import os
import sys
import yt_dlp
from pathlib import Path

from yt_dlp import YoutubeDL

class automateDownload:
    def __init__(self):
        pass

    def getUrlsInteractive(self):
        urls = []
        
        print("Youtube Video Downloader")
        print("Enter Youtube URLs (press Enter on empty line to finish):")

        while True:
            url = input(f"URL {len(urls) + 1}: ").strip()
            if not url:
                break
            urls.append(url)
        return urls
    
    def downloadVideos(self, urls):
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]/bestvideo',
            'merge_output_format': 'mp4',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'ignoreerrors': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for url in urls:
                try:
                    print(f"Downloading: {url}")
                    ydl.download([url])
                    print(f"Success: {url}")
                except Exception as e:
                    print(f"Failed: {url} - {e}")

    def main(self):
        urls = self.getUrlsInteractive()

        if not urls:
            print("No URLS provided!")
            sys.exit(1)
        
        print(f"\n Downloading {len(urls)} videos ...")
        self.downloadVideos(urls)

if __name__ == "__main__":
    downloader = automateDownload()
    downloader.main()