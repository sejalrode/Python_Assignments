#Sum of Digit.

iSum = 0
def SumDigit(No):
    global iSum
    if(No > 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10
        SumDigit(No)
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