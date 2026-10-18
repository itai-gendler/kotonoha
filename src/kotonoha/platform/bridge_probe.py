"""Probe a candidate bridge in a disposable process without creating a GUI."""

import argparse
from pathlib import Path

from .native_abi import load_bridge


def main() -> None:
    """Exit unsuccessfully if loading or Qt ABI validation fails."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bridge", type=Path)
    args = parser.parse_args()
    load_bridge(args.bridge)


if __name__ == "__main__":
    main()
