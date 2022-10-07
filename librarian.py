import os
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
