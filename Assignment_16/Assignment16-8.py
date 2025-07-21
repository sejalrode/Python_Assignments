#Remove all blank lines from a file.Save the cleaned output to a new file.

def RemoveBlankSpaces():
    fobj1 = open("Blank.txt","r")
    fobj2 = open("NewBlank.txt","w")

    data = fobj1.readlines()

    for line in data:
        if(line != "\n"):
            fobj2.write(line)

    fobj1.close()
    fobj2.close()
        
def main():
    RemoveBlankSpaces()

    print("Data written successfully")

if __name__ == "__main__":
    main()

'''

'''