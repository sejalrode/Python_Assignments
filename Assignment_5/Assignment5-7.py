#Area & Perimeter of Rectangle.

def CalculateArea(Value1,Value2):
    Ans = 1
    Ans = Value1 * Value2
    return Ans

def CalculatePerimeter(Value1,Value2):
    Ans = 1
    Ans = 2 * (Value1 + Value2)
    return Ans
    

def main():
    length = int(input("Enter length : "))
    breadth = int(input("Enter breadth : "))

    ret = CalculateArea(length, breadth)
    print("Area : ",ret)

    ret = CalculatePerimeter(length, breadth)
    print("Perimeter : ",ret)

if __name__ == "__main__":
    main()

'''
Enter length : 5
Enter breadth : 3

Area :  15
Perimeter :  16
'''