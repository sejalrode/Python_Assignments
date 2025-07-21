#Copy contents of one file into another file.

import os

def CopyFileContents(fname1,fname2):
    ret1 = os.path.exists(fname1)
    ret2 = os.path.exists(fname2)

    if(ret1 == True and ret2 == True):
        print("Both files are present in the current directory")
        fobj1 = open(fname1, "r")
        data = fobj1.read()

        fobj2 = open(fname2,"a")
        fobj2.write("\n"+data)

        fobj1.close()
        fobj2.close()

    else:
        print("There is no such file")

def main():

    FileName1 = input("Enter source filename : ")
    FileName2 = input("Enter destination filename : ")

    CopyFileContents(FileName1,FileName2)

    print("Contents copied successfully")

if __name__ == "__main__":
    main()

'''

'''