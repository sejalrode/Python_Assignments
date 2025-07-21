#Factorial of a number.

iCnt = 1
Fact = 1
def Factorial(No):
    global iCnt
    global Fact
    if(iCnt <= No):
        Fact = Fact * iCnt
        iCnt = iCnt + 1
        Factorial(No)
    

def main():
    Value = int(input("Enter a number : "))

    Factorial(Value)

    print("Factorial is : ",Fact)

if __name__ == "__main__":
    main()

'''
Enter a number : 5
Factorial is :  120
'''