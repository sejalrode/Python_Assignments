#Voting eligibility checker.

def CheckAge(Value):
    if(Value >= 18):
        return True
    return False

def main():
    no = int(input("Enter age : "))

    ret = CheckAge(no)
    if ret == True:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

if __name__ == "__main__":
    main()

'''
Enter age : 19
Eligible to vote
'''