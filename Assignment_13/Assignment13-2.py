class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount
    
    def Deposit(self):
        self.Amount = self.Amount + 1

    def Withdraw(self):
        self.Amount = self.Amount - 1

    def CalculateInterest(self):
        interest = self.Amount * BankAccount.ROI / 100
        print("Interest : ",interest)


    def Display(self):
        print("Name : "+self.Name)
        print("Amount : ",self.Amount)
    
def main():
    obj1 = BankAccount("Amit",20000)
    obj2 = BankAccount("Pooja",25000)
    
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()

    obj2.Deposit()
    obj2.Withdraw()
    obj2.CalculateInterest()
    obj2.Display()
    
if __name__ == "__main__":
    main()

'''
Interest :  2100.0
Name : Amit
Amount :  20000

Interest :  2625.0
Name : Pooja
Amount :  25000
'''