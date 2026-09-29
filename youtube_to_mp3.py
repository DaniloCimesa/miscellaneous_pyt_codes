import yt_dlp
url = input("Enter the URL of the video:")

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl":"%(title)s.%(ext)s",
    "ffmpeg_location": r"C:\Users\Danilo\OneDrive\Documents\variables\ffmpeg-2026-09-28-git-84779ade26-full_build\ffmpeg-2026-09-28-git-84779ade26-full_build\bin",  # adjust to your path
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    
print('Download completed!')