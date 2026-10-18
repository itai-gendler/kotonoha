#!/usr/bin/python3 -I
"""Build the distro bridge with local Qt; invoked by package-manager hooks."""

from __future__ import annotations

import argparse
import fcntl
import logging
import os
import signal
import subprocess
import tempfile
from pathlib import Path
from types import FrameType


class BuildInterrupted(Exception):
    """A process signal requested cancellation of an owned bridge build."""

    def __init__(self, signum: int) -> None:
        super().__init__(f"Bridge build interrupted by signal {signum}")
        self.signum: int = signum


def interrupt_build(signum: int, frame: FrameType | None) -> None:
    """Translate CLI termination into stack unwinding and child cleanup."""
    # A second termination request must not interrupt process-group cleanup.
    # main restores the caller's handlers after all resources have unwound.
    for watched in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
        signal.signal(watched, signal.SIG_IGN)
    raise BuildInterrupted(signum)


class NativeBridgeBuilder:
    """Serialize local builds and publish only a successfully loaded bridge.

    Source and state directories must be owned by the package administrator.
    Each subprocess has a timeout; temporary build trees are always removed.
    """

    def __init__(
        self, source_dir: Path, state_dir: Path, timeout: float = 300,
        *, python_executable: Path = Path("/usr/bin/python3"),
    ) -> None:
        self.source_dir: Path = source_dir
        self.state_dir: Path = state_dir
        self.timeout: float = timeout
        # Distro hooks use system Python so validation sees the user's system Qt.
        self.python_executable: Path = python_executable

    def rebuild(self) -> None:
        """Build, validate against system PyQt6, and atomically replace the bridge.

        Failures propagate to the package manager, preserving the previous file.
        A separate process loads the candidate so this process never retains an
        old Qt library across builds. Compilation runs outside the GUI lifecycle.
        """
        self.state_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
        self.state_dir.chmod(0o755)
        with (self.state_dir / "build.lock").open("w") as lock:
            # Package transactions serialize normally; also protect manual rebuilds.
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with tempfile.TemporaryDirectory(prefix="build-", dir=self.state_dir) as temporary:
                build_dir = Path(temporary)
                self._run([
                    "cmake", "-S", str(self.source_dir), "-B", str(build_dir),
                    "-DCMAKE_BUILD_TYPE=Release", "-DKOTONOHA_BUILD_BRIDGE=ON",
                    f"-DPython3_EXECUTABLE={self.python_executable}",
                ])
                self._run(["cmake", "--build", str(build_dir), "--parallel", "2"])
                candidate = build_dir / "libkoto-layer.so"
                self._run(self._probe_command(self.python_executable, candidate))
                candidate.chmod(0o755)
                os.replace(candidate, self.state_dir / "libkoto-layer.so")

    def _run(self, command: list[str]) -> None:
        """Run a bounded build step, making compiler failures visible to packaging."""
        with subprocess.Popen(command, start_new_session=True) as process:
            try:
                returncode = process.wait(timeout=self.timeout)
            except BaseException:
                # CMake owns compiler children: stop the entire process group
                # before removing its build tree, including on interruption.
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass  # The process group already exited; there is nothing to kill.
                process.wait()
                raise
            if returncode != 0:
                raise subprocess.CalledProcessError(returncode, command)

    @staticmethod
    def _probe_command(python_executable: Path, candidate: Path) -> list[str]:
        """Build an isolated ABI probe without importing the app package."""
        probe = "\n".join([
            "import ctypes,sys",
            "from PyQt6.QtCore import qVersion",
            "library=ctypes.CDLL(sys.argv[1])",
            "version=getattr(library,'koto_layer_qt_version',None)",
            "if version is not None:",
            " version.restype=ctypes.c_char_p",
            " built=version().decode('ascii')",
            " running=qVersion()",
            " def family(value):",
            "  parts=value.split('.')",
            "  valid=len(parts)>=3 and all(part.isdecimal() for part in parts[:3])",
            "  if not valid: raise OSError('Invalid Qt version: '+repr(value))",
            "  return tuple(int(part) for part in parts[:2])",
            " if family(built)!=family(running):",
            "  raise OSError(f'bridge built against Qt {built}, PyQt6 runtime is Qt {running}')",
        ])
        return [str(python_executable), "-I", "-c", probe, str(candidate)]


def main() -> int:
    """Rebuild the installed distro bridge, returning failure to its caller."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=Path("/usr/share/kotonoha/native"))
    parser.add_argument("--state-dir", type=Path, default=Path("/var/lib/kotonoha"))
    args = parser.parse_args()
    watched_signals = (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)
    previous = {signum: signal.getsignal(signum) for signum in watched_signals}
    try:
        for signum in watched_signals:
            signal.signal(signum, interrupt_build)
        NativeBridgeBuilder(args.source_dir, args.state_dir).rebuild()
    except BuildInterrupted as exc:
        logging.error("%s; retry with /usr/lib/kotonoha/rebuild-bridge", exc)
        return 128 + exc.signum
    except (OSError, subprocess.SubprocessError) as exc:
        logging.error(
            "Native bridge rebuild failed: %s. Previous bridge was preserved; "
            "it may be incompatible after a Qt update. "
            "Retry with sudo /usr/lib/kotonoha/rebuild-bridge", exc,
        )
        return 1
    finally:
        for signum, handler in previous.items():
            signal.signal(signum, handler)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
