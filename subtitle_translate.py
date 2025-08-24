import os
import re
from deep_translator import GoogleTranslator

# ---------------- Settings ----------------
input_srt = "C:/Users/User/video_directory/video.srt" #add the name of the video
output_srt = "C:/Users/User/video_directory/video.translated.srt"

translator = GoogleTranslator(source="ms", target="en")


def safe_translate(text):
    try:
        return translator.translate(text)
    except Exception:
        return "(translation unavailable)"


def process_srt(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = re.split(r"\n\n", content.strip())
    new_blocks = []
    for block in blocks:
        lines = block.splitlines()
        if len(lines) >= 3:
            idx = lines[0]
            timestamp = lines[1]
            text_ms = " ".join(lines[2:])

            text_en = safe_translate(text_ms)

            new_block = f"{idx}\n{timestamp}\n{text_ms}\n({text_en})"
            new_blocks.append(new_block)
        else:
            new_blocks.append(block)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(new_blocks))


if __name__ == "__main__":
    process_srt(input_srt, output_srt)
    print(f"Translated subtitles saved at: {output_srt}")
