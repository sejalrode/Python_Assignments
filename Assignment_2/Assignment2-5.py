#Accept one number from user and check whether it's prime number or not.

def Prime(iValue):
    if iValue < 2:
        return False  # 0 and 1 are not prime

    for i in range(2,iValue):
        if(iValue % i == 0):
            return False
    return True

def main():
    No = int(input("Enter a number : "))
    
    iRet = Prime(No)
    if(iRet == True):
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()

'''
Enter a number : 5
It is a prime number
'''