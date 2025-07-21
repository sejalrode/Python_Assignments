#Accept a no from user & print its factorial using for loop.

def Factorial(value):
    Fact = 1
    for i in range(1,value+1):
        Fact = Fact * i
    return Fact

def main():
    No = int(input("Enter a number : "))

    ret = Factorial(No)
    print(f"Factorial of {No} is : {ret}")
    
if __name__ == "__main__":
    main()

'''
Enter a number : 5
Factorial of 5 is : 120
'''