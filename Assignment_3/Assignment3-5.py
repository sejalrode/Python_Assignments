'''Accept N numbers from user & store it into List.Return addition of all prime no from that
list.Main python file accepts N no from user & pass each number to ChkPrime() function which
is part of user defined module named as MarvellousNum.Name of the function from main python
file should be ListPrime().'''

from MarvellousNum import ChkPrime

def ListPrime(PrimeData):
    sum = 0
    for i in PrimeData:
        sum = sum + i
    return sum
    
    
def main():
    size = int(input("Enter number of elements : "))

    Data = list()

    print("Input Elements :")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    PrimeData = list()
    
    for i in Data:
        iRet = ChkPrime(i)
        if iRet == True:
            PrimeData.append(i)

    Sum = ListPrime(PrimeData)
    
    print("Addition of Prime numbers : ",Sum)


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
10
34
2
5
8
Addition of Prime numbers :  32 (13 + 5 + 7 + 2 + 5)
'''