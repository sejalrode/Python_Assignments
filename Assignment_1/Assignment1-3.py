#Write a program which contains one functionnamed as Add() which accepts two numbersfrom user
#and return addition of that two numbers.

def Add(iNo1, iNo2):
    Ans = 0
    Ans = iNo1 + iNo2
    return Ans

def main():
    iValue1 = int(input("Enter first number : "))
    iValue2 = int(input("Enter second number : "))

    iRet = Add(iValue1,iValue2)

    print("Addition is : ",iRet)

if __name__ == "__main__":
    main()

'''
Enter first number : 11
Enter second number : 5
Addition is :  16
'''