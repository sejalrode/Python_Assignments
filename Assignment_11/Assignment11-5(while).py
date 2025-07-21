#Count 0 in a number.

def CountZero(No):
    Count = 0
    while(No > 0):
        iDigit = No % 10
        if(iDigit == 0):
            Count = Count + 1
        No = No // 10
    return Count

def main():
    Value = int(input("Enter a number : "))

    ret = CountZero(Value)

    print("Result is : ",ret)

if __name__ == "__main__":
    main()

'''
Enter a number : 1020300
Result is :  4
'''