#quick script to batch create folders from a UTF-8 encoded csv or txt file
#does not check if folders exist and probably won't work with other encodings
#==================================

import os
import sys
import re
import codecs

def main():
    path="sap_cikklista.txt"
    #path="test.txt"

    if not os.path.isfile(path):
        print("File {} does not exist",format(path))
        sys.exit()

    with codecs.open (path,'r',"utf-8") as infile:
        for line in infile:
            folderName=line.strip()
            folderName=folderName.translate({ord(c): None for c in '":/*?\%|<>'})
            os.mkdir(folderName)

if __name__ == '__main__':
   main()