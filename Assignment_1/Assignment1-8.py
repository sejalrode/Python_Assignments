#Write a program which accepts number from user and print that number of "*" on screen.

def main():
    iNo = int(input("Enter a number : "))

    for i in range(1,iNo+1):
        print(" * ", end = " ")

if __name__ == "__main__":
    main()

'''
Enter a number : 5
 *   *   *   *   *
'''