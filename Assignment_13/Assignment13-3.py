class Numbers:

    def __init__(self,no):
        self.value = no
    
    def ChkPrime(self):
        if self.value < 2:
            return False
        for i in range(2,self.value):
            if self.value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        perfect = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                perfect = perfect + i
        
        if(perfect == self.value):
            return True
        return False
    
    def Factors(self):
        print("Factors : ")
        for i in range(1,self.value+1):
            if self.value % i == 0:
                print(i, end = " ")

    def SumFactors(self):
        sum = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                sum = sum + i
        return sum        

    
def main():
    obj = Numbers(12)

    print("Prime : ",obj.ChkPrime())
    print("Perfect : ",obj.ChkPerfect())
    obj.Factors()
    print("\nSum of factors : ",obj.SumFactors())
    
if __name__ == "__main__":
    main()

'''
Prime :  False
Perfect :  False
Factors :
1 2 3 4 6 12
Sum of factors :  16
'''