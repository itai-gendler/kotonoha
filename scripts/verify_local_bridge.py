"""Verify the installed distro bridge, without requiring a running compositor."""

from pathlib import Path

import kotonoha
from kotonoha.platform.native_abi import load_bridge


def main() -> None:
    """Fail unless the package resolves to a local, ABI-compatible build."""
    bridge = Path(kotonoha.__file__).with_name("libkoto-layer.so")
    expected = Path("/var/lib/kotonoha/libkoto-layer.so")
    if not bridge.is_symlink() or bridge.resolve(strict=True) != expected:
        raise SystemExit(f"expected a locally built bridge at {expected}, found {bridge}")
    # Verify the same loading contract as application startup, without probing
    # a compositor (which would require a graphical session).
    load_bridge(bridge)


if __name__ == "__main__":
    main()
