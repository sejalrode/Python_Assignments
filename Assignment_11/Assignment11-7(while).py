#Print Pattern.

def Display(No):
    for i in range(No+1):
        for j in range(i):
            print(" * ", end = " ")
        print()

def main():
    Value = int(input("Enter a number : "))

    ret = Display(Value)

if __name__ == "__main__":
    main()

'''
Enter a number : 4

*
*   *
*   *   *
*   *   *   *
'''