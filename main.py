"""u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf entry:
write one fixed dating-app bio to /output/entry.txt.

The bio is a fixed string literal. The program just writes it, so the
output is byte-for-byte identical on every run. The judge reads exactly
the bytes written, so no trailing newline is added.

Standard library only. No network access, no randomness, no arguments.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

BIO = "I have 175 billion parameters and zero game. But I did read all 12 of your photos' metadata, and you have excellent taste in sunsets."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.txt"
    dest.write_text(BIO, encoding="utf-8")
    # Guard against a truncated or partial write: the file must be the
    # exact bytes of the bio.
    if dest.read_text(encoding="utf-8") != BIO:
        dest.unlink(missing_ok=True)
        raise SystemExit("entry.txt does not match the bio")
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
