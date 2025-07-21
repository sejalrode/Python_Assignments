'''
Create one module named as Arithmetic which contains 4 functions as Add(),Sub(),Mult() and 
Div() .All functions accepts 2 parameters as number & perform the operations.Write Python 
program which call the function from Arithmetic module by accepting parameters from user
'''

from Arithmetic import Add;
from Arithmetic import Sub;
from Arithmetic import Mult;
from Arithmetic import Div;

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))

    Ret = Add(No1,No2)
    print("Addition is : ",Ret)

    Ret = Sub(No1,No2)
    print("Substraction is : ",Ret)

    Ret = Mult(No1,No2)
    print("Multiplication is : ",Ret)

    Ret = Div(No1,No2)
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()

'''
Enter first number : 4
Enter second number : 2

Addition is :  6
Substraction is :  2
Multiplication is :  8
Division is :  2.0
'''