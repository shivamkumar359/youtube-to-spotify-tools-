# YouTube Watch Later → Clean Titles Extractor

A Python tool to extract real YouTube video titles from a Watch Later playlist and clean them for music platforms like Spotify.

## Features
- Extracts real YouTube titles using yt-dlp
- Removes reupload / remix terms:
  - slow + reverb
  - remix
  - nightcore
  - lyrics
  - official video / audio
- Outputs Spotify-ready titles
- Handles unavailable videos safely

## Requirements
- Python 3.8+
- yt-dlp

## Installation
```bash
pip install -r requirements.txt
