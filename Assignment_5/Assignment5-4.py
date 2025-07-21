#Find largest among 3 numbers.

def CheckMax(Value1, Value2, Value3):
    if Value1 >= Value2:
        if Value1 >= Value3:
            return Value1
        else:
            return Value3
    else:
        if Value2 >= Value3:
            return Value2
        else:
            return Value3

def main():
    # taking 3 inputs at a time
    no1, no2, no3 = map(int, input("Enter 3 numbers : ").split())

    ret = CheckMax(no1,no2,no3)
    
    print("Largest number is : ",ret)

if __name__ == "__main__":
    main()

'''
Enter 3 numbers : 5 9 3
Largest number is :  9
'''