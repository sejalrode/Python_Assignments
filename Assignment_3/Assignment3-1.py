#Accept N numbers from user and store it into List.Return addition of all elements from that 
#List.

def Sum(Values):
    iSum = 0
    for i in Values:
        iSum = iSum + i
    return iSum

def main():
    size = int(input("Enter number of elements : "))

    Data = list()

    print("Input Elements :")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    iRet = Sum(Data)

    print("Sum is : ",iRet)

if __name__ == "__main__":
    main()

'''
Enter number of elements : 6
Input Elements :
13
5
45
7
4
56
Sum is :  130
'''