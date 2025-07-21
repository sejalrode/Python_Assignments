#Sum of first N Natural numbers.

sum = 0 
def SumNatural(No):
    global sum
    if(No >= 1):
        sum = sum + No
        No = No - 1
        SumNatural(No)
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