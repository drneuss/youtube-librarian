from os import listdir
from os.path import isfile, join
import re
def main():
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    currentdl = onlyfiles.open("r")
    x = re.search("", currentdl)
