#Count no of lines,words & characters from file.

import os
import sys

def CountFrequency():

    fobj = open("Hello.txt","r")

    ret = os.path.exists("Hello.txt")

    if(ret == True):
        print("Files is present in the current directory")
        data = fobj.read()

        lcount = 0 ; wcount = 0; ccount = 0

        for i in data:
            if (i == "\n"):
                lcount = lcount + 1
            ccount = ccount + 1

        # Add 1 to line count if file is not empty and doesn't end with newline
        if len(data) > 0 and data[-1] != '\n':
            lcount = lcount + 1

        words = data.split()   # Split file content into words

        for i in words:
                wcount = wcount + 1

        print("No of lines : ",lcount)
        print("No of words : ",wcount)
        print("No of characters : ",ccount)

        fobj.close()

    else:
        print("There is no such file")

def main():
    CountFrequency()

if __name__ == "__main__":
    main()

'''
Files is present in the current directory
No of lines :  4
No of words :  8
No of characters :  57
'''