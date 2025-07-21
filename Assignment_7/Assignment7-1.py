#2 lambda functions to calculate square & cube of a number.

Square = lambda No : No * No
Cube = lambda No : No * No * No

def main():
    Value = int(input("Enter a number : "))

    ret = Square(Value)
    print("Square : ",ret)

    ret = Cube(Value)
    print("Cube : ",ret)

if __name__ == "__main__":
    main()

'''
Enter a number : 3
Square :  9
Cube :  27
'''