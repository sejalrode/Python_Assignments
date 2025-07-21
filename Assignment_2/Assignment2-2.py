#Accept one number and display pattern.

def main():
    No = int(input("Enter a number : "))
    for i in range(No):
        for j in range(No):
            print(" * ",end = " ")
        print()


if __name__ == "__main__":
    main()

'''
Enter a number : 5
 *   *   *   *   *
 *   *   *   *   *
 *   *   *   *   *
 *   *   *   *   *
 *   *   *   *   *
 '''