Windows batchfiles to help create video libraries with youtube-dl
Downloads videos in the best available quality. For youtube videos with maximum resolution below 480p downloads the "best" marked format and the best quality video stream.


Place youtube-dl.exe in the current folder.
Place the contents of the FFMPEG build archive in "/resources/ffmpegfolder/" so that ffmpeg.exe is located at "\resources\ffmpegfolder\bin\ffmpeg.exe"





Enter video urls in "urls.txt"
Run "run.bat", it will run on a loop. 
Let it loop several times over the list of video urls in "urls.txt".
Then run "check.bat". 
If it does not reach the end of the list then the video it stops at is missing.
Remove that video url from urls.txt and rerun/recheck.
For non-youtube videos use urls-nonyoutube.txt and run-nonyoutube.bat
Run rename.bat to rename video output folder with date and time once task is complete




Intermediary pages are located in "dump_*" folder(s) for debugging.



Just download this repository as a zip file, extract to preferred location and you're good to go! 




2022-07-18                                                         Dr Neuss

youtube-dl                                                      v2021.12.17

DOWNLOAD                                            https://youtube-dl.org/

README         https://github.com/ytdl-org/youtube-dl/blob/master/README.md

SUPPORTED SITES   https://ytdl-org.github.io/youtube-dl/supportedsites.html
