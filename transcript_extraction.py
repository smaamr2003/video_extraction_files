import whisper
import os
from deep_translator import GoogleTranslator

# Path to your video file
video_path = "C:\\Users\\smaam\\Documents\\Rakib_Abdullah_files\\Malay_Syarahan_dan_Kuliah\\1860038654555960.mp4"

# Load Whisper model (you can change "small" to "medium", "large", etc.)
model = whisper.load_model("small")

# Transcribe the video
result = model.transcribe(video_path, language="ms")  # "ms" for Malay (or leave out language for auto-detect)
segments = result["segments"]

# Initialize Google Translator
translator = GoogleTranslator(source="ms", target="en")

# Get the folder and base filename of the video
video_dir = os.path.dirname(video_path)         # e.g. C:\Users\...\Malay_Syarahan_dan_Kuliah
video_name = os.path.splitext(os.path.basename(video_path))[0]  # e.g. my_video

# Create transcript filename in same folder
transcript_path = os.path.join(video_dir, f"{video_name}.txt")

# Save transcript
with open(transcript_path, "w", encoding="utf-8") as f:
    for seg in segments:
        start = seg["start"]
        end = seg["end"]
        text_ms = seg["text"].strip()

        # Translate Malay to English
        text_en = translator.translate(text_ms)

        f.write(f"[{start:.2f} --> {end:.2f}]\n{ text_ms }\n({ text_en})\n\n")

print(f"Transcript saved at: {transcript_path}")

# ---------- Save Subtitles (.srt) ----------
srt_path = os.path.join(video_dir, f"{video_name}.srt")

def format_timestamp(seconds: float) -> str:
    """Convert seconds to SRT timestamp format."""
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds * 1000) % 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

with open(srt_path, "w", encoding="utf-8") as f:
    for i, seg in enumerate(segments, start=1):
        start = format_timestamp(seg["start"])
        end = format_timestamp(seg["end"])
        text_ms = seg["text"].strip()

        # Translate Malay to English
        text_en = translator.translate(text_ms)

        f.write(f"{i}\n{start} --> {end}\n{text_ms}\n({text_en})\n\n")

print(f"Subtitle file saved at: {srt_path}")
