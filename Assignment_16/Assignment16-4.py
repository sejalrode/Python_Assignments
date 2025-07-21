#Accept 10 no from users & write them into a file named numbers.txt each on a new line.

import os

def WriteFile(data):
    fobj = open("numbers.txt","w")

    for no in data:
        fobj.write(str(no) + "\n")

    fobj.close()

def main():
    print("Enter 10 numbers : ")
    no = []
    for i in range(1,11):
        data = int(input())
        no.append(data)

    WriteFile(no)

    print("Data written successfully")

if __name__ == "__main__":
    main()

'''

'''