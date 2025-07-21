'''Create a class Product with attributes name & price.Implement __eq__ method to compare 2
products if they are equal in price.'''

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __eq__(self,other):
        return self.price == other.price
 
def main():
    pobj1 = Product("Amit",55000)
    pobj2 = Product("Smita",55000)

    if(pobj1 == pobj2):
        print("The 2 products are equal in price")
    else:
        print("The 2 products are not equal in price")

if __name__ == "__main__":
    main()

'''
The 2 products are equal in price
'''
# __eq__ is a special callback method (also called a magic method)
# It is automatically called when using '=='
# Returns True if the two objects have the same price
# Used to define custom logic for equality comparison
