'''Create a class BankAccount with account_number,name & balance.Use __init__ & create methods for
deposit,withdraw & displaying balance.'''

class BankAccount:

    def __init__(self,accountno,name,balance):
        self.account_number = accountno
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ",amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn: ",amount)

    def DisplayBalance(self):
        print("Account Holder: ",self.name)
        print("Account Number: ",self.account_number)
        print("Current Balance: ",self.balance)
        
def main():
    bobj = BankAccount(1234567890, "Amit", 5000)

    # Display initial balance
    bobj.DisplayBalance()

    # Perform deposit
    bobj.deposit(1500)

    # Perform withdrawal
    bobj.withdraw(2000)

    # Final balance
    bobj.DisplayBalance()

    
if __name__ == "__main__":
    main()

'''
Account Holder:  Amit
Account Number:  1234567890
Current Balance:  5000
Deposited:  1500
Withdrawn:  2000

Account Holder:  Amit
Account Number:  1234567890
Current Balance:  4500
'''