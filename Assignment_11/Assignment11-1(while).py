#Print numbers from 1 to N.

def Display(No):
    iCnt = 1
    while(iCnt <= No):
        print(iCnt)
        iCnt = iCnt + 1

def main():
    Value = int(input("Enter a number : "))

    Display(Value)

if __name__ == "__main__":
    main()

'''
Enter a number : 5
1
2
3
4
5
'''