import os
import subprocess
import sys

def download(url):
    vname = url.split("?v=")[1]
    cmd = f"yt-dlp -q -f 140 {url} -o {vname}.mp3"
    os.system(cmd)


if __name__ == "__main__":
    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    
    for url in lines:
        download(url)

