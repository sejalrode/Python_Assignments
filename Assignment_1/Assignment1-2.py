#Write a program which contains one function named as ChkNum() which accept one parameter as
#number.If number is evenit should display "Even number" atherwise display "Odd number"

def ChkNum(iValue):
    if iValue % 2 == 0:
        return 1
    else:
        return -1

def main():
    iNo = int(input("Enter a number : "))

    iRet = ChkNum(iNo)
    if iRet == 1:
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()


'''
Enter a number : 11
Odd number
Enter a number : 44
Even number
'''