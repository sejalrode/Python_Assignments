#Create a file marks.txt with student named & marks,Then read the file & display student 
# who scored more than 75 marks.

def DisplayFileContents():
    fobj1 = open("marks.txt","w")

    print("Writing Data into file")
    fobj1.write("Amit 65")
    fobj1.write("\nSumit 85")
    fobj1.write("\nRahul 95")
    fobj1.write("\nAtul 55")
    fobj1.close()

    fobj2 = open("marks.txt", "r")
    data = fobj2.readlines()

    print("Students who scored more than 75 marks : ")

    for line in data:
        name,marks = line.strip().split()

        mark = int(marks)
        if (mark > 75):
            print(f"{name} {marks}")

    fobj2.close()
        
def main():
    DisplayFileContents()

if __name__ == "__main__":
    main()

'''

'''