#Write a program which accept name from user & display length of its name.

def Strlen(name):
    count = 0
    for char in name:
        count = count + 1
    return count

def main():
    name = input("Enter the name : ")
    
    iRet = Strlen(name)
    print(iRet)

if __name__ == "__main__":
    main()

'''
Enter the name : Marvellous
10
'''