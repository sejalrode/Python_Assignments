'''Create a class Book with private attribute __price .Add methods to get and set the price.
show encapsulation.'''

class Book:
    def __init__(self,value):
        self.__price = value

    def setprice(self,new_value):
        self.__price = new_value
    
    def getprice(self):
        return self.__price
        
def main():
    bobj = Book(25000)
    print("Initial price : ",bobj.getprice())

    bobj.setprice(35000)
    print("Updated price : ",bobj.getprice())
    
if __name__ == "__main__":
    main()

'''
Initial price :  25000
Updated price :  35000
'''