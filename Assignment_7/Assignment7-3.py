#Accept a list of integers from user & use filter() to keep only even numbers.

Even = lambda No : (No % 2 == 0)

def main():
    Data = []

    size = int(input("Enter number of elements : "))

    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    FData = list(filter(Even,Data))
    print("Even numbers : ",FData)

if __name__ == "__main__":
    main()

'''
Enter number of elements : 6
Enter the elements :
1
2
3
4
5
6
Even numbers :  [2, 4, 6]
'''