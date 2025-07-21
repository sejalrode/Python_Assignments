#Accept filenames from user & compare all contents of the file.Accept filename using command line arguments.

import os
import sys

def CompareFileContents(fname1,fname2):
    ret1 = os.path.exists(fname1)
    ret2 = os.path.exists(fname2)

    if(ret1 == True and ret2 == True):
        print("Both files are present in the current directory")
        fobj1 = open(fname1, "r")
        data1 = fobj1.read()

        fobj2 = open(fname2,"r")
        data2 = fobj2.read()

        if(data1 == data2):
            print("Success")
        else:
            print("Failure")

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
            print("Filename1.txt Filename2.txt")
        
    if(len(sys.argv) == 3):
        CompareFileContents(sys.argv[1],sys.argv[2])
    
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()

'''
Both files are present in the current directory
Success
'''