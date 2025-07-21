#Lambda function which accepts 2 parameter and returns its multiplication.

Multiplication = lambda Value1, Value2 : Value1 * Value2

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    iRet = Multiplication(No1,No2)

    print("Multiplication is : ",iRet) 

if __name__ == "__main__":
    main()

'''
Enter first number : 4
Enter second number : 3
Multiplication is :  12
'''