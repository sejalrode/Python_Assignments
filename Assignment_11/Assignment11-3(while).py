#Sum of Digit.

def SumDigit(No):
    iSum = 0
    while(No > 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10
    return iSum

def main():
    Value = int(input("Enter a number : "))

    ret = SumDigit(Value)

    print("Sum of digits : ",ret)

if __name__ == "__main__":
    main()

'''
Enter a number : 1234
Sum of digits :  10
'''