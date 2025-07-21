#Print numbers from 1 to N.

iCnt = 1
def Display(No):
    global iCnt    
    if (iCnt <= No):
        print(iCnt)
        iCnt = iCnt + 1
        Display(No)

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