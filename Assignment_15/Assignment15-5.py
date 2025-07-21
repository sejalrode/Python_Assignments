#Accept filenames & string from user & return frequency of that string from file.

import os
import sys

def StringFrequency(fname,string):
    ret = os.path.exists(fname)

    if(ret == True):
        print("Files is present in the current directory")
        fobj = open(fname, "r")
        data = fobj.read()

        count = 0

        words = data.split()   # Split file content into words

        for i in words:
            if(i == string):
                count = count + 1

        fobj.close()

        return count

    else:
        print("There is no such file")

def main():

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to copy file contents")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("Filename.txt String")
        
    if(len(sys.argv) == 3):
        ret = StringFrequency(sys.argv[1],sys.argv[2])
        print("Frequency of string is : ",ret)

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()

'''
Files is present in the current directory
Frequency of string is :  3
'''