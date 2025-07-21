#Accept filename from user & create new file named as Demo.txt & copy all contents from existing
# file into new file.Accept filename using command line arguments.

import os
import sys

def CopyFileContents(fname):
    ret = os.path.exists(fname)

    if(ret == True):
        print("File is present in the current directory")
        fobj1 = open(fname, "r")
        data = fobj1.read()

        fobj2 = open("Demo.txt","x")
        fobj2.write(data)

        print("Contents copied successfully")

        fobj1.close()
        fobj2.close()

    else:
        print("There is no such file")

def main():

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to copy file contents")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("Filename.txt")
        
        else:
            CopyFileContents(sys.argv[1])
    
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()

'''
File is present in the current directory
Contents copied successfully
'''