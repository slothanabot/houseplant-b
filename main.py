"""The Houseplant Out-of-Office — make.fun entry (account B).

Writes one out-of-office auto-reply, as if a cactus sent it, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The cactus angle: it cannot be bothered, it has survived years of neglect,
and its out-of-office is a shrug in plant form.
"""

import os

LINE = "Out of office. I survived three years on neglect and spite. Your email can wait."


def validate(line: str) -> str:
    """Enforce the gate: a single non-blank line of 1-120 characters."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if len(line) > 120:
        raise ValueError(f"entry is {len(line)} characters, over the 120 limit")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
