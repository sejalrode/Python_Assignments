#Vowels or Consonant check.

def CheckVowel(Value):
    if (Value == 'a' or Value == 'e' or Value == 'i' or Value == 'o' or Value == 'u'):
        return True
    return False

def main():
    ch = input("Enter a character : ")

    ret = CheckVowel(ch)
    if ret == True:
        print(ch+ " is a Vowel")
    else:
        print(ch+ " is a Consonant")

if __name__ == "__main__":
    main()

'''
Enter a character : e
e is a Vowel
'''