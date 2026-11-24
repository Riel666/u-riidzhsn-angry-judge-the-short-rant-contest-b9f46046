"""One short rant about a small everyday annoyance, under 400 characters.
"""

import os

TEXT = "The office printer has one job and it has chosen violence: it jams on page one, prints page two in a font last seen in 1997, then blinks 'PC LOAD LETTER' like I personally insulted its ancestors. I did not insult its ancestors. I just wanted one page."


def main():
    assert 1 <= len(TEXT) <= 400, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
