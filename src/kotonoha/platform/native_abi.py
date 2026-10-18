"""Validate the bridge against the Qt actually loaded by PyQt6.

The PyQt6 compile-time Qt version is not the runtime library version. All bridge
consumers use this boundary, including the isolated package-install probe.
"""

from __future__ import annotations

import ctypes
from pathlib import Path


def validate_qt_versions(built: str, running: str) -> None:
    """Reject malformed versions and different Qt major/minor ABI families."""
    versions: list[tuple[int, int]] = []
    for version in (built, running):
        parts = version.split(".")
        if len(parts) < 3 or not all(part.isdecimal() for part in parts[:3]):
            raise OSError(f"Invalid Qt version: {version!r}")
        versions.append((int(parts[0]), int(parts[1])))
    if versions[0] != versions[1]:
        raise OSError(f"bridge built against Qt {built}, PyQt6 runtime is Qt {running}")


def validate_bridge(library: ctypes.CDLL) -> None:
    """Check the optional native ABI handshake against the running Qt.

    Symbol discovery is limited to this external ctypes compatibility boundary.
    TODO: require the handshake once pre-handshake bridges are unsupported.
    """
    from PyQt6.QtCore import qVersion

    version = getattr(library, "koto_layer_qt_version", None)
    if version is None:
        return
    version.restype = ctypes.c_char_p
    raw_version: bytes | None = version()
    if raw_version is None:
        raise OSError("Bridge returned no Qt version")
    try:
        built = raw_version.decode("ascii")
    except UnicodeDecodeError as exc:
        raise OSError("Bridge returned an invalid Qt version") from exc
    validate_qt_versions(built, qVersion())


def load_bridge(path: Path) -> ctypes.CDLL:
    """Load system Qt first, then load and validate a native bridge candidate."""
    from PyQt6 import QtCore

    QtCore.qVersion()
    library = ctypes.CDLL(str(path))
    validate_bridge(library)
    return library
