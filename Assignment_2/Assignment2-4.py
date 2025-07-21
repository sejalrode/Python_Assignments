#Accept one number from user and return addition of its factors.

def AddFactors(iValue):
    result = 0
    for i in range(1,iValue):
        if(iValue % i == 0):
            result = result + i

    return result

def main():
    No = int(input("Enter a number : "))
    
    iRet = AddFactors(No)

    print("Addition of factors is : ",iRet)

if __name__ == "__main__":
    main()

'''
Enter a number : 12
Addition of factors is :  16 (1+2+3+4+6)
 '''