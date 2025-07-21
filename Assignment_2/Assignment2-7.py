#Accept one number and display pattern.

def main():
    No = int(input("Enter a number : "))
    for i in range(No):
        for j in range(1,No+1):
            print(j,end = " ")
        print()


if __name__ == "__main__":
    main()

'''
Enter a number : 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''