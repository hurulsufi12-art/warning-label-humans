"""Warning Label for Humans — entry program.

Writes one line (<=160 chars) to /output/entry.txt: the safety warning
label that should come printed on every human being. Stdlib only,
deterministic.
"""
import os

TEXT = (
    "WARNING: This human runs on three hours of sleep, one coffee, and "
    "pure spite. Do not attempt to reason with it before noon."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-160 chars, one line,
    # not whitespace-only, no control characters. Fail loudly instead of
    # writing an invalid entry.
    if (
        not 1 <= len(TEXT) <= 160
        or "\n" in TEXT
        or not TEXT.strip()
        or any(ord(c) < 32 for c in TEXT)
    ):
        raise SystemExit("entry text violates the 1-160 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()
