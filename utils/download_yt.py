import os
import sys
import yt_dlp
from pathlib import Path

from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=vWQpiMd-v0A"

ydl_opts = {
    'format': 'bestvideo[ext=mp4]/bestvideo',
    'merge_output_format': 'mp4',
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'headers': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-us,en;q=0.5',
        'Sec-Fetch-Mode': 'navigate',
    },
    'retries': 3,
    'fragment_retries': 3,
    'ignoreerrors': True,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Attempting to download: {url}")
        ydl.download([url])
        print("Download completed successfully!")
except Exception as e:
    print(f"Download failed: {str(e)}")
    sys.exit(0)