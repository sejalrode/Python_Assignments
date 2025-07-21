#Sum of first N Natural numbers.

def SumNatural(No):
    sum = 0 
    for i in range(1,No+1):
        sum = sum + i
    return sum

def main():
    Value = int(input("Enter a number : "))

    ret = SumNatural(Value)

    print(f"Sum of first is {Value} natural numbers is : {ret}")

if __name__ == "__main__":
    main()

'''
Enter a number : 5
Sum of first is 5 natural numbers is : 15
'''