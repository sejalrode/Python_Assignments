#Accept N numbers from user and store it into List.Return minimum number from that List.

def Min(Values):
    iMin = Values[0]
    for i in Values:
        if(iMin > i):
            iMin = i
    return iMin

def main():
    size = int(input("Enter number of elements : "))

    Data = list()

    print("Input Elements :")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    iRet = Min(Data)

    print("Minimum number is : ",iRet)

if __name__ == "__main__":
    main()

'''
Enter number of elements : 4
Input Elements :
13
5
45
7
Minimum number is :  5
'''