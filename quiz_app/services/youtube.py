import yt_dlp
import os

def extract_youtube_info(url: str) -> dict:
    ydl_opts = {
        "quiet": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return ydl.sanitize_info(info)


def download_audio(url: str, video_id: str) -> str:
    output_dir = "media/audio"
    os.makedirs(output_dir, exist_ok=True)

    output_path = f"{output_dir}/{video_id}.%(ext)s"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "quiet": True,
        "noplaylist": True,
        "ffmpeg_location": "/opt/homebrew/bin",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return f"{output_dir}/{video_id}.mp3"
