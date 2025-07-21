#Accept one number from user and return number of digits in that number.

def Digit(iValue):
    iCount = 0
    while(iValue > 0 ):
        iValue = iValue // 10
        iCount = iCount + 1
    return iCount

def main():
    No = int(input("Enter a number : "))
    
    iRet = Digit(No)

    print("No of digits are : ",iRet)

if __name__ == "__main__":
    main()

'''
Enter a number : 5187934
No of digits are :  7
'''