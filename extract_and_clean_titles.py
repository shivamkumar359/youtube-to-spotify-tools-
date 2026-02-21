import subprocess
import re

INPUT_FILE = "watch_later_urls.txt"
OUTPUT_FILE = "video_titles_cleaned.txt"

# Words / phrases to remove
REMOVE_PATTERNS = [
    r"\bslow(?:ed)?\b",
    r"\breverb\b",
    r"\bslow\s*\+\s*reverb\b",
    r"\bsped\s*up\b",
    r"\bnightcore\b",
    r"\bremix\b",
    r"\breuploaded\b",
    r"\breupload\b",
    r"\blyrics?\b",
    r"\bofficial\s*video\b",
    r"\bofficial\s*audio\b",
    r"\baudio\b",
    r"\bvisualizer\b",
    r"\bmv\b"
]

def clean_title(title: str) -> str:
    title = title.lower()

    for pattern in REMOVE_PATTERNS:
        title = re.sub(pattern, "", title, flags=re.IGNORECASE)

    # remove brackets and extra symbols
    title = re.sub(r"[\[\]\(\)\|]", "", title)

    # normalize spaces
    title = re.sub(r"\s{2,}", " ", title).strip()

    # Capitalize properly for Spotify search
    return title.title()

titles = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    urls = f.read().splitlines()

for i, url in enumerate(urls, start=1):
    try:
        result = subprocess.run(
            ["yt-dlp", "--get-title", url],
            capture_output=True,
            text=True,
            timeout=20
        )

        raw_title = result.stdout.strip()

        if raw_title:
            cleaned = clean_title(raw_title)
            titles.append(cleaned)
            print(f"{i}. {cleaned}")
        else:
            titles.append("UNAVAILABLE VIDEO")
            print(f"{i}. UNAVAILABLE VIDEO")

    except Exception:
        titles.append("UNAVAILABLE VIDEO")
        print(f"{i}. UNAVAILABLE VIDEO")

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for t in titles:
        out.write(t + "\n")

print("\nDONE")
print(f"Clean titles saved to: {OUTPUT_FILE}")
