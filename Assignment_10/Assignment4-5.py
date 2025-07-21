'''Write a program which contains filter(),map() and reduce() in it.Python application which 
contains one list of numbers.List contains the numbers which are accepted from user.Filter
should filter out all prime numbers.Map function will multiply each number by 2.
Reduce will return maximum that numbers.'''

from functools import reduce

def CheckPrime(No):
    if No < 2 :
        return False
    for i in range(2,No):
        if No % i == 0:
            return False
    return True

def Multiply(No):
    return No * 2

def Maximum(A,B):
    Max = A
    if A < B:
        Max = B
    else:
        Max = A
    return Max


def main():
    size = int(input("Enter number of elements : "))

    Data = list()

    print("Enter the values : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List : ",Data)

    FData = list(filter(CheckPrime,Data))
    print("List after filter : ",FData)

    MData = list(map(Multiply,FData))
    print("List after map : ",MData)

    RData = reduce(Maximum,MData)
    print("Output of reduce : ",RData)


if __name__ == "__main__":
    main()

'''
Enter number of elements : 8
Enter the values :
2
70
11
10
17
23
31
77
Input List :  [2, 70, 11, 10, 17, 23, 31, 77]
List after filter :  [2, 11, 17, 23, 31]
List after map :  [4, 22, 34, 46, 62]
Output of reduce :  62
'''