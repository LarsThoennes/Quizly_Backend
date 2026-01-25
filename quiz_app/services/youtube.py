import yt_dlp
import os

def extract_youtube_info(url: str) -> dict:
    """
    Extracts metadata information from a YouTube video.

    - Uses yt-dlp to fetch video details without downloading the video
    - Disables playlist processing
    - Returns sanitized video information as a dictionary
    """
    ydl_opts = {
        "quiet": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return ydl.sanitize_info(info)


def download_audio(url: str, video_id: str) -> str:
    """
    Downloads and converts YouTube video audio to an MP3 file.

    - Creates an output directory if it does not exist
    - Downloads the best available audio stream
    - Converts the audio to MP3 format using FFmpeg
    - Returns the file path of the generated audio file
    """
    output_dir = "media/audio"
    os.makedirs(output_dir, exist_ok=True)

    output_path = f"{output_dir}/{video_id}.%(ext)s"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,
        "quiet": True,
        "noplaylist": True,
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
