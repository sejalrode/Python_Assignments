#Accept a list of integers from user & use reduce() to find product of numbers.

from functools import reduce

Product = lambda No1, No2 : No1 * No2

def main():
    Data = []

    size = int(input("Enter number of elements : "))

    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    RData = reduce(Product,Data)
    print("Product : ",RData)

if __name__ == "__main__":
    main()

'''
Enter number of elements : 3
Enter the elements :
2
3
4
Product :  24
'''