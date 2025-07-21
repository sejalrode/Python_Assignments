#Power function.

def Power(No1,No2):
    result = 1
    for i in range(No2):
        result = result * No1
    return result

def main():
    Value1 = int(input("Enter a number : "))
    Value2 = int(input("Enter the power : "))

    ret = Power(Value1, Value2)

    print("Result is : ",ret)

if __name__ == "__main__":
    main()

'''
Enter a number : 2
Enter the power : 3
Result is :  8
'''