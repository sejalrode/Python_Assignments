#Accept a string & check whether it is a palindrome  or not.

def Palindrome(String):
    Reverse = ""
    Length = len(String)
    for i in range(Length-1,-1,-1):
        Reverse = Reverse + String[i]
    
    if(Reverse == String):
        return True
    else:
        return False

def main():
    Input = input("Enter a string : ")

    ret = Palindrome(Input)
    if(ret == True):
        print(f"{Input} is Palindrome")
    else:
        print(f"{Input} is not Palindrome")

if __name__ == "__main__":
    main()

'''
Enter a string : radar
radar is Palindrome
'''