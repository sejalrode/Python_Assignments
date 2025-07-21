#Write a program which accept number from user and check whether that number is positive or 
#negative or zero.

def ChkNum(iNo):
    if iNo > 0 :
        print("Positive Number")
    elif iNo < 0:
        print("Negative Number")
    else :
        print("Zero")

def main():
    iValue = int(input("Enter a number : "))

    ChkNum(iValue)

if __name__ == "__main__":
    main()

'''
Enter a number : 11
Positive Number
Enter a number : -8
Negative Number
Enter a number : 0
Zero
'''