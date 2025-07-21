#Lambda function which accepts one parameter and returns power of 2.

Power = lambda Value : Value ** 2

def main():
    No = int(input("Enter a number : "))

    iRet = Power(No)

    print(iRet) 

if __name__ == "__main__":
    main()

'''
Enter a number : 4
16
'''