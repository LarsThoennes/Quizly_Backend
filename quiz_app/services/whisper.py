import whisper
import os

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes an audio file into text using the Whisper model.

    - Validates that the audio file exists
    - Loads the Whisper transcription model
    - Converts speech to text
    - Returns the transcribed text content
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    model = whisper.load_model("turbo")
    result = model.transcribe(file_path)

    return result["text"]
