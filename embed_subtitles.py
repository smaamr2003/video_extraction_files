import os
import subprocess

# ---------------- Settings ----------------
video_file = "C:/Users/User/Video_directory/video.mp4"
subs_file = "C:/Users/User/Video_directory/video_translated.srt"
output_file = "C:/Users/User/Video_directory/video_with_subs.mp4"


def embed_subs(video, subs, output):
    cmd = [
        "ffmpeg",
        "-i", video,
        "-vf", f"subtitles={subs}:force_style='FontName=Arial,FontSize=20'",
        "-c:a", "copy",
        output,
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    embed_subs(video_file, subs_file, output_file)
    print(f"Final video with subtitles saved at: {output_file}")
