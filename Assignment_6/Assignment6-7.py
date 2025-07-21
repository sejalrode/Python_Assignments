#Accept 5 no from user & print Largest number.

def Maximum(value):
    Max = value[0]
    for i in value:
        if(i > Max):
            Max = i
    return Max

def main():
    print("Enter 5 numbers : ")
    Data = list()
    for i in range(5):
        No = int(input())
        Data.append(No)
    
    ret = Maximum(Data)

    print("Maximum number is : ",ret)
    
if __name__ == "__main__":
    main()

'''
Enter 5 numbers :
23
89
12
56
45
Maximum number is :  89
'''