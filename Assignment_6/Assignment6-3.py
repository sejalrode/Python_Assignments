#Print sum of even numbers from 1 to 100 using loop.

def SumEven():
    sum = 0
    for i in range(2,102,2):
        sum = sum + i
    return sum

def main():
    ret = SumEven()
    print("Sum of even numbers between 1 to 100 is : ",ret)
    
if __name__ == "__main__":
    main()

#Sum of even numbers between 1 to 100 is :  2550