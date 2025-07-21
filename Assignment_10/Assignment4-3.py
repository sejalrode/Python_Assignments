'''Write a program which contains filter(),map() and reduce() in it.Python application which 
contains one list of numbers.List contains the numbers which are accepted from user.Filter
should filter out all such numbers which greater than or equal to 70 & less than or equal to
90.Map function will increase each number by 10.Reduce will return product of all that numbers.'''

from functools import reduce

Sort = lambda No : No >= 70 and No <= 90
Increase = lambda No : No + 10
Product = lambda A,B : A * B

def main():
    size = int(input("Enter number of elements : "))

    Data = list()

    print("Enter the values : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List : ",Data)

    FData = list(filter(Sort,Data))
    print("List after filter : ",FData)

    MData = list(map(Increase,FData))
    print("List after map : ",MData)

    RData = reduce(Product,MData)
    print("Output of reduce : ",RData)


if __name__ == "__main__":
    main()

'''
Enter number of elements : 12
Enter the values :
4
34
36
76
68
24
89
23
86
90
45
70
Input List :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter :  [76, 89, 86, 90, 70]
List after map :  [86, 99, 96, 100, 80]
Output of reduce :  6538752000
'''