#Create a text file named as student.txt & write names of 5 students in it.

import os

def WriteFile():
    fobj = open("student.txt","x")

    fobj.write("Amit\n")
    fobj.write("Smita\n")
    fobj.write("Rahul\n")
    fobj.write("Sumit\n")
    fobj.write("Diya\n")

    fobj.close()

def main():

    WriteFile()

    print("Data written successfully")

if __name__ == "__main__":
    main()

'''

'''