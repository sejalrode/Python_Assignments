'''Create a class Calculator with methods for add,subtract,multiply,divide.Ask user input for
values & call methods accordingly.'''

class Calculator:

    def __init__(self,value1,value2):
        self.no1 = value1
        self.no2 = value2
    
    def Addition(self):
        add = self.no1 + self.no2
        return add
    
    def Substraction(self):
        sub = self.no1 - self.no2
        return sub
    
    def Multiplication(self):
        mult = self.no1 * self.no2
        return mult
    
    def Division(self):
        div = self.no1 / self.no2
        return div

def main():
    value1 = int(input("Enter first no : "))
    value2 = int(input("Enter second no : "))

    cobj = Calculator(value1,value2)

    print("Addition is : ",cobj.Addition())
    print("Substraction is : ",cobj.Substraction())
    print("Multiplication is : ",cobj.Multiplication())
    print("Division is : ",cobj.Division())
    
    
if __name__ == "__main__":
    main()

'''
Enter first no : 10
Enter second no : 5

Addition is :  15
Substraction is :  5
Multiplication is :  50
Division is :  2.0
'''