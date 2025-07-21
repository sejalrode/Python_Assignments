#Factorial of a number.

def Factorial(No):
    iCnt = 1
    Fact = 1
    while(iCnt <= No):
        Fact = Fact * iCnt
        iCnt = iCnt + 1
    print("Factorial is : ",Fact)

def main():
    Value = int(input("Enter a number : "))

    Factorial(Value)

if __name__ == "__main__":
    main()

'''
Enter a number : 5
Factorial is :  120
'''