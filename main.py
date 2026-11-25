"""The Router Confesses — make.fun bounty entry.

A home Wi-Fi router excuses itself for dropping the connection at the
climax of a movie. This script writes the entry line to a file.
"""

import os
import sys

ENTRY = "You only ever notice me when I stop working, so I stopped at the exact second you'd feel it most."

TITLE = "Stopped to Be Noticed"


def resolve_output_path():
    """Pick where the entry goes.

    ENTRY_OUTPUT wins outright. Otherwise an output directory from
    OUTPUT_DIR or MAKEFUN_OUTPUT_DIR gets entry.txt appended, and the
    fallback is /output/entry.txt.
    """
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return os.path.join("/output", "entry.txt")


def main():
    if not ENTRY or not ENTRY.strip():
        raise SystemExit("entry must not be empty")
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    output_path = resolve_output_path()
    data = ENTRY.encode("utf-8")
    parent = os.path.dirname(os.path.abspath(output_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "wb") as handle:
        handle.write(data)
    os.chmod(output_path, 0o644)
    with open(output_path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit("read-back check failed: written file differs from entry")


if __name__ == "__main__":
    main()
