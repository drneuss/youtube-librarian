:a
youtube-dl.exe -a ".\urls-nonyoutube.txt" -i -o ".\videos\%%(title)s-%%(id)s.%%(ext)s" -f "bestvideo+bestaudio/best" --merge-output-format "mkv" --ffmpeg-location ".\resources\ffmpegfolder\bin\ffmpeg.exe" --cookies ".\cookies.txt" --write-pages
move.bat
goto a