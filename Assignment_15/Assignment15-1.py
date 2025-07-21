#Accept filename from user & check whether that file exists in current directory or not.

import os

def ChkFile(fname):
    ret = os.path.exists(fname)

    if(ret == True):
        print("File is present in the current directory")
    else:
        print("There is no such file")

def main():
    print("Enter the filename : ")
    filename = input()

    ChkFile(filename)

if __name__ == "__main__":
    main()

'''
Enter the filename :
Python.txt
File is present in the current directory
'''