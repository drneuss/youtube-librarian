import os
if not os.path.exists("urls.txt"):
    with open('urls.txt', 'w+') as urls:
        urls.close()
if not os.path.exists("urls-nonyoutube.txt"):
    with open('urls-nonyoutube.txt', 'w+') as urln:
        urln.close()
if not os.path.exists("viddb.txt"):
    with open('viddb.txt', 'w+') as vdb:
        vdb.close()
if not os.path.exists("viddb-ny.txt"):
    with open('viddb-ny.txt', 'w+') as vdbn:
        vdbn.close()
if not os.path.exists("cookies.txt"):
    with open('cookies.txt', 'w+') as cookies:
        cookies.close()
if not os.path.exists("run.bat"):
    with open('run.bat', 'w+') as runyd:
        runyd.writelines([r":a"+"\n", "youtube-dl.exe -a \".\\urls.txt\" -i -o \".\\videos\\%%(title)s-%%(format_id)s-%%(width)s-%%(height)s-%%(id)s.%%(ext)s\" -f \"bestvideo[height>=480]+bestaudio/best+bestvideo\" --merge-output-format \"mkv\" --ffmpeg-location \".\resources\ffmpegfolder\bin\ffmpeg.exe\" --cookies \".\cookies.txt\" --write-pages"+"\n", r"move.bat"+"\n", r"goto a"])
if not os.path.exists("run-nonyoutube.bat"):
    with open('run-nonyoutube.bat', 'w+') as rnny:
        rnny.writelines([r":a"+"\n", "youtube-dl.exe -a \".\\urls-nonyoutube.txt\" -i -o \".\\videos\\%%(title)s-%%(id)s.%%(ext)s\" -f \"bestvideo+bestaudio/best\" --merge-output-format \"mkv\" --ffmpeg-location \".\\resources\\ffmpegfolder\\bin\\ffmpeg.exe\" --cookies \".\\cookies.txt\" --write-pages"+"\n", r"move.bat"+"\n", r"goto a"])
if not os.path.exists("rename.bat"):
    with open('rename.bat', 'w+') as renamer:
        renamer.writelines([r"set _my_datetime=%date%_%time%"+"\n", r"set _my_datetime=%_my_datetime: =_%"+"\n", r"set _my_datetime=%_my_datetime::=%"+"\n", r"set _my_datetime=%_my_datetime:/=_%"+"\n", r"set _my_datetime=%_my_datetime:.=_%"+"\n", r"rename videos \"videos_%_my_datetime%\""])
if not os.path.exists("check.bat"):
    with open('check.bat', 'w+') as checker:
        checker.writelines(["youtube-dl.exe -a \".\\urls.txt\" -o \".\\videos\\%%(title)s-%%(format_id)s-%%(width)s-%%(height)s-%%(id)s.%%(ext)s\" -f \"bestvideo[height>=480]+bestaudio/best+bestvideo\" --merge-output-format \"mkv\" --ffmpeg-location ".\\resources\\ffmpegfolder\\bin\\ffmpeg.exe\" --cookies \".\\cookies.txt\" --write-pages"+"\n", r"move.bat"])
if not os.path.exists("move.bat"):
    with open('move.bat', 'w+') as mover:
        mover.writelines([r"set _my_datetime=%date%_%time%"+"\n", r"set _my_datetime=%_my_datetime: =_%"+"\n", r"set _my_datetime=%_my_datetime::=%"+"\n", r"set _my_datetime=%_my_datetime:/=_%"+"\n", r"set _my_datetime=%_my_datetime:.=_%"+"\n", r"md dump_%_my_datetime%"+"\n", "move \".\\*.dump\" \".\\dump_%_my_datetime%\\\""])
if not os.path.exists("youtube-dl.exe"):
    import urllib.request
    ydlexe = urllib.request.urlopen('https://youtube-dl.org/downloads/latest/youtube-dl.exe')
    with open('youtube-dl.exe','wb') as output:
        output.write(ydlexe.read())
if not os.path.exists("videos"):
    os.makedirs("videos")
if not os.path.exists("resources/ffmpegfolder"):
    os.makedirs("resources/ffmpegfolder")
answer = input("Enter list of links in urls.txt for youtube videos and urls-nonyoutube.txt for non-youtube videos. Then press Y for youtube and N for non-youtube videos:")
if answer == "Y":
    os.system("run.bat")
#list current directory
    currentfiles = os.listdir("videos")
    strcurrfiles = "\n".join(currentfiles)
# Open the file in append & read mode ('a+')
    with open("viddb.txt", "a+") as file_object:
    # Move read cursor to the start of file.
        file_object.seek(0)
    # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
    # Append text at the end of file
        file_object.write(strcurrfiles)
elif answer == "N":
    os.system("run-nonyoutube.bat")
#list current directory
    currentfiles = os.listdir("videos")
    strcurrfiles = "\n".join(currentfiles)
# Open the file in append & read mode ('a+')
    with open("viddb-ny.txt", "a+") as file_object:
    # Move read cursor to the start of file.
        file_object.seek(0)
    # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
    # Append text at the end of file
        file_object.write(strcurrfiles)
file_object.close()
