#Accept a no from user & check whether it is prime or not.

def CheckPrime(value):
    if value < 2:
        return False
    for i in range(2,value):
        if(value % i == 0):
            return False
    return True

def main():
    No = int(input("Enter a number : "))

    ret = CheckPrime(No)
    if(ret == True):
        print(f"{No} is a prime number")
    else:
        print(f"{No} is not a prime number")

if __name__ == "__main__":
    main()

'''
Enter a number : 11
11 is a prime number
'''