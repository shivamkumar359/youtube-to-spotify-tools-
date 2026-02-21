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


## Why this exists
YouTube Watch Later cannot be shared or exported. This guide shows a clean,
repeatable way to extract real video titles and prepare them for Spotify.

## What this is NOT
- Not a YouTube downloader
- Not a Spotify scraper
- Not a playlist mirroring tool

## Limitations
- Deleted / private videos cannot be recovered
- Spotify availability varies by region
