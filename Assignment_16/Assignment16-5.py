#Read a file line by line & display only those lines that contains more than 5 words.

import os

def DisplayFile(FileName):
    fobj = open(FileName,"r")

    wcount = 0

    Lines = fobj.readlines()

    for line in Lines:
        words = line.split()
        wcount = 0

        for word in words:
            wcount = wcount + 1

        if(wcount > 5):
            print(line)

    fobj.close()

def main():
    FileName = input("Enter filename : ")

    DisplayFile(FileName)

if __name__ == "__main__":
    main()

'''
Enter filename : Hello.txt

Python Marvellous is a Python Programming batch

LB Marvellous is a Logic building batch
'''