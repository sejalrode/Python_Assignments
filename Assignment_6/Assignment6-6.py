#Print triangle pattern.

def Pattern(value):
    for i in range(value+1):
        for j in range(i):
            print(" * ", end = " ")
        print()

def main():
    No = int(input("Enter a number : "))

    Pattern(No)

if __name__ == "__main__":
    main()

'''
Enter a number : 4

 *
 *   *
 *   *   *
 *   *   *   *
'''