class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self,value):
        self.radius = value
    
    def CalculateArea(self):
        self.area = Circle.PI * self.radius*self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Area : ",self.area)
        print("Circumference : ",self.circumference)

def main():
    value = float(input("Enter radius of circle : "))
    obj1 = Circle()
    obj1.Accept(value)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()
    

if __name__ == "__main__":
    main()

'''
Enter radius of circle : 2.0
Area :  12.56
Circumference :  12.56
'''