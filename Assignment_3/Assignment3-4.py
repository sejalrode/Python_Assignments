#Accept N numbers from user and store it into List.Accept another no and return frequency of that no.

def Frequency(No,Values):
    iCount = 0
    for i in Values:
        if(i == No):
            iCount = iCount + 1
    return iCount

def main():
    size = int(input("Enter number of elements : "))

    Data = list()

    print("Input Elements :")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    iNo = int(input("Element to search : "))
    iRet = Frequency(iNo,Data)

    print("Frequency is : ",iRet)

if __name__ == "__main__":
    main()

'''
Enter number of elements : 11
Input Elements :
13
5
45
7
4
56
5
34
2
5
65
Element to search : 5
Frequency is :  3
'''