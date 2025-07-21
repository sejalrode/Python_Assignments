#Write a program which contains one function that accept one number from user and returns true
#if number is divisible by 5 otherwise return false.

def ChkDivisible(iNo):
    if iNo % 5 == 0:
        return True
    else :
        return False

def main():
    iValue = int(input("Enter a number : "))

    iRet = ChkDivisible(iValue)

    print(iRet)

if __name__ == "__main__":
    main()

'''
Enter a number : 8
False
Enter a number : 25
True
'''