#Accept a no from user & print its multiplication table upto 10.

def Table(value):
    for i in range(1,11):
        print(f"{value} x {i} = {value * i}")

def main():
    No = int(input("Enter a number : "))

    Table(No)
    
if __name__ == "__main__":
    main()

'''
Enter a number : 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
'''