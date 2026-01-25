import whisper
import os

def transcribe_audio(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    model = whisper.load_model("turbo")
    result = model.transcribe(file_path)

    return result["text"]
