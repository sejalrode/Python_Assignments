#Accept filename from user & open that file & display contents of file on screen.

import os

def DisplayFileContents(fname):
    ret = os.path.exists(fname)

    if(ret == True):
        print("File is present in the current directory")
        fobj = open(fname, "r")
        data = fobj.read()

        print("Data from file is : ",data)

        fobj.close()

    else:
        print("There is no such file")

def main():
    print("Enter the filename that you want to read: ")
    filename = input()

    DisplayFileContents(filename)

if __name__ == "__main__":
    main()

'''
Enter the filename that you want to read:
Python.txt
File is present in the current directory

Data from file is :  Jay Ganesh...
Python Marvellous
'''