#Accept N numbers from user and store it into List.Return maximum number from that List.

def Max(Values):
    iMax = Values[0]
    for i in Values:
        if(iMax < i):
            iMax = i
    return iMax

def main():
    size = int(input("Enter number of elements : "))

    Data = list()

    print("Input Elements :")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    iRet = Max(Data)

    print("Maximum number is : ",iRet)

if __name__ == "__main__":
    main()

'''
Enter number of elements : 7
Input Elements :
13
5
45
7
4
56
34
Maximum number is :  56
'''