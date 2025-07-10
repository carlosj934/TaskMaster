import os
import sys
import yt_dlp
from pathlib import Path

from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=vWQpiMd-v0A"

ydl_opts = {
    'format': 'bestvideo[ext=mp4]/bestvideo',
    'merge_output_format': 'mp4',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])