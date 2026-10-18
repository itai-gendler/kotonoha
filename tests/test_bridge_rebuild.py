"""Behavioral evidence for local bridge publication and build failure cleanup."""

from __future__ import annotations

import fcntl
import os
import select
import signal
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1]))

from kotonoha.platform.native_abi import load_bridge, validate_qt_versions  # noqa: E402
from scripts.rebuild_bridge import NativeBridgeBuilder  # noqa: E402

PROJECT_ROOT = Path(__file__).parents[1]


@pytest.fixture
def native_source(tmp_path: Path) -> Path:
    """Compile a real tiny shared library exposing the bridge's ABI handshake."""
    version = subprocess.check_output(
        [sys.executable, "-I", "-c", "from PyQt6.QtCore import qVersion; print(qVersion())"],
        text=True,
    ).strip()
    source = tmp_path / "source"
    source.mkdir()
    (source / "CMakeLists.txt").write_text(
        "cmake_minimum_required(VERSION 3.20)\n"
        "project(test_bridge LANGUAGES C)\n"
        "add_library(koto-layer SHARED bridge.c)\n"
    )
    (source / "bridge.c").write_text(f'const char* koto_layer_qt_version(void) {{ return "{version}"; }}\n')
    return source


def test_deferred_cmake_install_needs_no_qt_and_contains_no_native_binary(tmp_path: Path) -> None:
    """Distro payloads must configure without Qt and never ship a CI-built bridge."""
    build = tmp_path / "build"
    dest = tmp_path / "install"
    subprocess.run([
        "cmake", "-S", str(PROJECT_ROOT), "-B", str(build),
        "-DKOTONOHA_BUILD_BRIDGE=OFF", "-DCMAKE_DISABLE_FIND_PACKAGE_Qt6=ON",
        f"-DCMAKE_INSTALL_PREFIX={dest}",
    ], check=True)
    subprocess.run(["cmake", "--build", str(build)], check=True)
    subprocess.run(["cmake", "--install", str(build)], check=True)
    assert not list(dest.rglob("*.so"))
    assert (dest / "share/licenses/kotonoha/LICENSE").is_file()


def test_successful_repeated_build_replaces_old_bridge(native_source: Path, tmp_path: Path) -> None:
    """Installation and subsequent triggers publish usable, readable native code."""
    state = tmp_path / "state"
    builder = NativeBridgeBuilder(native_source, state, python_executable=Path(sys.executable))
    builder.rebuild()
    output = state / "libkoto-layer.so"
    assert output.read_bytes().startswith(b"\x7fELF")
    assert output.stat().st_mode & 0o777 == 0o755
    output.write_bytes(b"obsolete bridge")
    builder.rebuild()
    assert output.read_bytes().startswith(b"\x7fELF")
    assert not list(state.glob("build-*"))


@pytest.mark.parametrize("failure", ["compiler", "abi"])
def test_failed_build_preserves_previous_bridge_and_cleans_worktree(
    native_source: Path, tmp_path: Path, failure: str,
) -> None:
    """Neither compiler failure nor an incompatible candidate may replace the bridge."""
    state = tmp_path / "state"
    state.mkdir()
    output = state / "libkoto-layer.so"
    output.write_bytes(b"previous bridge")
    code = "invalid C" if failure == "compiler" else 'const char* koto_layer_qt_version(void) { return "1.0.0"; }'
    (native_source / "bridge.c").write_text(code)
    with pytest.raises(subprocess.CalledProcessError):
        NativeBridgeBuilder(native_source, state, python_executable=Path(sys.executable)).rebuild()
    assert output.read_bytes() == b"previous bridge"
    assert not list(state.glob("build-*"))


def test_concurrent_rebuild_is_rejected(native_source: Path, tmp_path: Path) -> None:
    """A manual rebuild must not race a package transaction's publication."""
    state = tmp_path / "state"
    state.mkdir()
    with (state / "build.lock").open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with pytest.raises(BlockingIOError):
            NativeBridgeBuilder(native_source, state, python_executable=Path(sys.executable)).rebuild()
    assert not (state / "libkoto-layer.so").exists()


def test_timeout_cleans_build_and_allows_retry(native_source: Path, tmp_path: Path) -> None:
    """A stuck build has a deadline, releases its lock, and removes temporary output."""
    state = tmp_path / "state"
    cmake = native_source / "CMakeLists.txt"
    original = cmake.read_text()
    cmake.write_text(original + 'execute_process(COMMAND "${CMAKE_COMMAND}" -E sleep 30)\n')
    with pytest.raises(subprocess.TimeoutExpired):
        NativeBridgeBuilder(native_source, state, timeout=0.1, python_executable=Path(sys.executable)).rebuild()
    assert not list(state.glob("build-*"))
    assert not (state / "libkoto-layer.so").exists()
    cmake.write_text(original)
    NativeBridgeBuilder(native_source, state, python_executable=Path(sys.executable)).rebuild()
    assert (state / "libkoto-layer.so").is_file()


@pytest.mark.parametrize("signum", [signal.SIGTERM, signal.SIGINT, signal.SIGHUP])
def test_cli_termination_stops_compiler_cleans_and_allows_retry(
    native_source: Path, tmp_path: Path, signum: int,
) -> None:
    """Package-manager termination must stop children and unwind the build lock."""
    state = tmp_path / "state"
    state.mkdir()
    output = state / "libkoto-layer.so"
    output.write_bytes(b"previous bridge")
    ready = tmp_path / "ready"
    os.mkfifo(ready)
    worker = tmp_path / "worker.py"
    worker.write_text(
        "import os, signal\n"
        f"with open({str(ready)!r}, 'w') as ready:\n"
        "    ready.write(str(os.getpid()))\n"
        "signal.pause()\n"
    )
    cmake = native_source / "CMakeLists.txt"
    original = cmake.read_text()
    cmake.write_text(original + f'execute_process(COMMAND "{sys.executable}" "{worker}")\n')
    descriptor = os.open(ready, os.O_RDONLY | os.O_NONBLOCK)
    child_pid: int | None = None
    try:
        with subprocess.Popen([
            sys.executable, "-I", str(PROJECT_ROOT / "scripts/rebuild_bridge.py"),
            "--source-dir", str(native_source), "--state-dir", str(state),
        ]) as process:
            try:
                assert select.select([descriptor], [], [], 10)[0], "compiler did not start"
                child_pid = int(os.read(descriptor, 128))
                process.send_signal(signum)
                assert process.wait(timeout=10) == 128 + signum
            finally:
                if process.poll() is None:
                    process.kill()
                    process.wait()
        child_status = Path(f"/proc/{child_pid}/stat")
        # A killed orphan may await init's reaping; it must no longer execute.
        assert not child_status.exists() or child_status.read_text().split(") ", 1)[1].startswith("Z")
        assert output.read_bytes() == b"previous bridge"
        assert not list(state.glob("build-*"))
    finally:
        os.close(descriptor)
        if child_pid is not None:
            try:
                os.kill(child_pid, signal.SIGKILL)
            except ProcessLookupError:
                pass  # Cleanup after a failing regression against the old CLI.
    cmake.write_text(original)
    NativeBridgeBuilder(native_source, state, python_executable=Path(sys.executable)).rebuild()


def test_loader_checks_running_qt_rather_than_pyqt_compile_version(
    native_source: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Installation and application loading accept the same running Qt ABI."""
    from PyQt6 import QtCore

    state = tmp_path / "state"
    NativeBridgeBuilder(native_source, state, python_executable=Path(sys.executable)).rebuild()
    monkeypatch.setattr(QtCore, "QT_VERSION_STR", "1.0.0")
    load_bridge(state / "libkoto-layer.so")
    monkeypatch.setattr(QtCore, "qVersion", lambda: "1.0.0")
    with pytest.raises(OSError, match="PyQt6 runtime is Qt 1.0.0"):
        load_bridge(state / "libkoto-layer.so")


@pytest.mark.parametrize("built,running", [
    ("6.10.1", "6.10.2"), ("6.11.0", "6.11.0"),
])
def test_qt_abi_accepts_matching_minor_versions(built: str, running: str) -> None:
    validate_qt_versions(built, running)


@pytest.mark.parametrize("built,running", [
    ("6.10.1", "6.11.1"), ("5.10.1", "6.10.1"), ("6.10", "6.10.1"),
    ("invalid", "6.10.1"), ("6.10.1", "invalid"),
])
def test_qt_abi_rejects_incompatible_or_malformed_versions(built: str, running: str) -> None:
    with pytest.raises(OSError):
        validate_qt_versions(built, running)


def test_cli_build_failure_reports_recovery_preserves_old_file_and_allows_retry(
    native_source: Path, tmp_path: Path,
) -> None:
    """An installer gets failure plus recovery guidance, never a false success."""
    state = tmp_path / "state"
    state.mkdir()
    output = state / "libkoto-layer.so"
    output.write_bytes(b"previous bridge")
    source = native_source / "bridge.c"
    original = source.read_text()
    source.write_text("invalid C")
    result = subprocess.run([
        sys.executable, "-I", str(PROJECT_ROOT / "scripts/rebuild_bridge.py"),
        "--source-dir", str(native_source), "--state-dir", str(state),
    ], capture_output=True, text=True, timeout=20)
    assert result.returncode == 1
    assert "Previous bridge was preserved" in result.stderr
    assert "sudo /usr/lib/kotonoha/rebuild-bridge" in result.stderr
    assert output.read_bytes() == b"previous bridge"
    assert not list(state.glob("build-*"))
    source.write_text(original)
    NativeBridgeBuilder(native_source, state, python_executable=Path(sys.executable)).rebuild()
    load_bridge(output)
