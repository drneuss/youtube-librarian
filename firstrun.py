with open('urls.txt', 'w+')
with open('urls-nonyoutube.txt', 'w+')
with open('viddb.txt', 'w+')
with open('viddb-ny.txt', 'w+')
with open('cookies.txt', 'w+')
with open('run.bat', 'w+') as run
    run.writelines([":a", "youtube-dl.exe -a ".\urls.txt" -i -o ".\videos\%%(title)s-%%(format_id)s-%%(width)s-%%(height)s-%%(id)s.%%(ext)s" -f "bestvideo[height>=480]+bestaudio/best+bestvideo" --merge-output-format "mkv" --ffmpeg-location ".\resources\ffmpegfolder\bin\ffmpeg.exe" --cookies ".\cookies.txt" --write-pages", "move.bat", "goto a"])
with open('run-nonyoutube.bat', 'w+') as rnny
    rnny.writelines([":a", "youtube-dl.exe -a ".\urls-nonyoutube.txt" -i -o ".\videos\%%(title)s-%%(id)s.%%(ext)s" -f "bestvideo+bestaudio/best" --merge-output-format "mkv" --ffmpeg-location ".\resources\ffmpegfolder\bin\ffmpeg.exe" --cookies ".\cookies.txt" --write-pages", "move.bat", "goto a"])
with open('rename.bat', 'w+') as renamer
    renamer.writelines(["set _my_datetime=%date%_%time%", "set _my_datetime=%_my_datetime: =_%", "set _my_datetime=%_my_datetime::=%", "set _my_datetime=%_my_datetime://=_%", "set _my_datetime=%_my_datetime:.=_%", "rename videos "videos_%_my_datetime%""])
with open('check.bat', 'w+') as checker
    checker.writelines(["youtube-dl.exe -a ".\urls.txt" -o ".\videos\%%(title)s-%%(format_id)s-%%(width)s-%%(height)s-%%(id)s.%%(ext)s" -f "bestvideo[height>=480]+bestaudio/best+bestvideo" --merge-output-format "mkv" --ffmpeg-location ".\resources\ffmpegfolder\bin\ffmpeg.exe" --cookies ".\cookies.txt" --write-pages", "move.bat"])
with open('move.bat', 'w+') as mover
    mover.writelines(["set _my_datetime=%date%_%time%", "set _my_datetime=%_my_datetime: =_%", "set _my_datetime=%_my_datetime::=%", "set _my_datetime=%_my_datetime://=_%", "set _my_datetime=%_my_datetime:.=_%", "md dump_%_my_datetime%"", "move ".\*.dump" ".\dump_%_my_datetime%\""])
