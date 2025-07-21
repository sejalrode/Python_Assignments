#Even Odd check.

def CheckEvenOdd(Value):
    if(Value % 2 == 0):
        return True
    return False

def main():
    no = int(input("Enter a number : "))

    ret = CheckEvenOdd(no)
    if ret == True:
        print(no, " is an even number")
    else:
        print(no, " is an odd number")

if __name__ == "__main__":
    main()

'''
Enter a number : 17
17  is an odd number
'''