import os
import subprocess

# ---------------- Settings ----------------
video_url = "https://www.facebook.com/VIDEO_ID"  # Change this
output_dir = "C:\\Users\\User\\Video_directory"
os.makedirs(output_dir, exist_ok=True)


def download_video_and_subs(url, outdir):
    cmd = [
        "yt-dlp",
        "--write-auto-subs",   # download auto subtitles if available
        "--sub-lang", "all",    # grab ALL available auto-subtitles regardless of language
        "--convert-subs", "srt",
        "-f", "mp4",           # force MP4 video
        "-o", os.path.join(outdir, "%(id)s.%(ext)s"),
        url,
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    download_video_and_subs(video_url, output_dir)
    print(f"Video and subtitles downloaded to: {output_dir}")
