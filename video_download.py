import yt_dlp

# URL of the video you want to download
url = ""

# Download options
ydl_opts = {
    # Pick best mp4 video + best m4a audio
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',

    # Save location and filename format (uncomment to input the directory)
    # 'outtmpl': # 'directory of the video' + '\\%(id)s.%(ext)s', 
    # Saves according to the ID of the video for videos with longer names 

    # Always merge into MP4 container
    'merge_output_format': 'mp4',

    # Avoid problematic characters in filenames
    'restrictfilenames': True
}

# Run download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
