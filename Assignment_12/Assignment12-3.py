class Arithmetic:
    PI = 3.14

    def __init__(self):
        self.value1 = 0.0
        self.value2 = 0.0

    def Accept(self,no1,no2):
        self.value1 = no1
        self.value2 = no2
    
    def Addition(self):
        self.add = self.value1 + self.value2
        return self.add

    def Substraction(self):
        self.sub = self.value1 - self.value2
        return self.sub

    def Multiplication(self):
        self.mult = self.value1 * self.value2
        return self.mult

    def Division(self):
        self.div = self.value1 // self.value2
        return self.div

def main():
    obj1 = Arithmetic()
    obj1.Accept(25,5)
    ret = print("Addition : ",obj1.Addition())
    ret = print("Substraction : ",obj1.Substraction())
    ret = print("Multiplication : ",obj1.Multiplication())
    ret = print("Division : ",obj1.Division())

    obj2 = Arithmetic()
    obj2.Accept(100,10)
    ret = print("Addition : ",obj2.Addition())
    ret = print("Substraction : ",obj2.Substraction())
    ret = print("Multiplication : ",obj2.Multiplication())
    ret = print("Division : ",obj2.Division())

if __name__ == "__main__":
    main()

'''
Addition :  30
Substraction :  20
Multiplication :  125
Division :  5

Addition :  110
Substraction :  90
Multiplication :  1000
Division :  10
'''