:a
youtube-dl.exe -a ".\urls.txt" -i -o ".\videos\%%(title)s-%%(format_id)s-%%(width)s-%%(height)s-%%(id)s.%%(ext)s" -f "bestvideo[height>=480]+bestaudio/best+bestvideo" --merge-output-format "mkv" --ffmpeg-location ".\resources\ffmpegfolder\bin\ffmpeg.exe" --cookies ".\cookies.txt" --write-pages
move.bat
goto a