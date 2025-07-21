#Print Pattern.

def Display(n):
    if n == 0:
        return
    Display(n - 1)
    print("*   " * n)
    
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