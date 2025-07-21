#Accept one number from user and return addition of digits in that number.

def DigitSum(iValue):
    iSum = 0
    while(iValue > 0 ):
        iDigit = iValue % 10
        iSum = iSum + iDigit
        iValue = iValue // 10
    return iSum

def main():
    No = int(input("Enter a number : "))
    
    iRet = DigitSum(No)

    print("Sum of digits is : ",iRet)

if __name__ == "__main__":
    main()

'''
Enter a number : 5187934
Sum of digits is :  37
'''