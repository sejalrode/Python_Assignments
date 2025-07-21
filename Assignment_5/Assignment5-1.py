#Arithmetic Operations on 2 numbers.

def Sum(Value1, Value2):
    Ans = 0
    Ans = Value1 + Value2
    return Ans

def Difference(Value1, Value2):
    Ans = 0
    Ans = Value1 - Value2
    return Ans

def Product(Value1, Value2):
    Ans = 0
    Ans = Value1 * Value2
    return Ans

def Division(Value1, Value2):
    Ans = 0
    Ans = Value1 / Value2
    return Ans

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    ret = Sum(No1, No2)
    print("Sum : ",ret)

    ret = Difference(No1, No2)
    print("Difference : ",ret)

    ret = Product(No1, No2)
    print("Product : ",ret)

    ret = Division(No1, No2)
    print("Division : ",ret)

if __name__ == "__main__":
    main()

'''
Enter first number : 10
Enter second number : 2

Sum :  12
Difference :  8
Product :  20
Division :  5.0
'''