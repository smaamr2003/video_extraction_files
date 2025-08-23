import yt_dlp

# URL of the video you want to download
url = "https://www.facebook.com/share/v/19eLnMqERY/"

# Download options
ydl_opts = {
    # Pick best mp4 video + best m4a audio
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',

    # Save location and filename format
    'outtmpl': 'C:\\Users\\smaam\\Documents\\Rakib_Abdullah_files\\Malay_Syarahan_dan_Kuliah\\%(id)s.%(ext)s',

    # Always merge into MP4 container
    'merge_output_format': 'mp4',

    # Avoid problematic characters in filenames
    'restrictfilenames': True
}

# Run download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
