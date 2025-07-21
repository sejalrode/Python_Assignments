#Accept one number from user and return its factorial.

def Factorial(iValue):
    result = 1
    for i in range(1,iValue+1):
        result = result * i
    return result

def main():
    No = int(input("Enter a number : "))
    
    iRet = Factorial(No)

    print("Factorial is : ",iRet)

if __name__ == "__main__":
    main()

'''
Enter a number : 5
Factorial is :  120
 '''