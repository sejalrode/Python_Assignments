#Accept a list of integers from user & use filter() to keep only prime numbers.

def Prime(Value):
    for i in range(2,Value):
        if( Value % i == 0):
            return False
    return True

def main():
    Data = []

    size = int(input("Enter number of elements : "))

    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)
    
    FData = list(filter(Prime,Data))
    print("Prime numbers : ",FData)

if __name__ == "__main__":
    main()

'''
Enter number of elements : 8
Enter the elements :
10
11
12
13
14
15
16
17
Prime numbers :  [11, 13, 17]
'''