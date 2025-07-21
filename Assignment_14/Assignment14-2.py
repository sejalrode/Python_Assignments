class Rectangle:
    def __init__(self,value1,value2):
        self.length = value1
        self.width = value2

    def Area(self):
        area = self.length * self.width
        print("Area : ",area)
    
    def Circumferecne(self):
        circumference = 2 * (self.length + self.width)
        print("Circumference  : ",circumference)

def main():
    obj1 = Rectangle(10,5)
    obj2 = Rectangle(8,2)

    obj1.Area()
    obj1.Circumferecne()

    obj2.Area()
    obj2.Circumferecne()

if __name__ == "__main__":
    main()

'''
Area :  50
Circumference  :  30

Area :  16
Circumference  :  20
'''