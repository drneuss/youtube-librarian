from os import listdir
from os.path import isfile, join
from subprocess import Popen
import re
def main():
    p = Popen("run.bat", cwd=r".\run.bat") #run.bat
    stdout, stderr = p.communicate()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))] #outputfilelist
    currentdl = onlyfiles.open("r")
    x = re.search("", currentdl)
