'''Create a class Vehicle with method start().Derive class Car & override the method start()
with additional behaviour.Show method overriding.'''

class Vehicle:
    
    def Start(self):
        print("Inside self of Base")
    
class Car(Vehicle):
    def Start(self):
        print("Inside self of Derived")
        print("Car class")
        
def main():
    vobj = Vehicle()
    cobj = Car()

    print("Calling start() from Vehicle:")
    vobj.Start()

    print("\nCalling start() from Car:")
    cobj.Start()
    
if __name__ == "__main__":
    main()

'''
Calling start() from Vehicle:
Inside self of Base

Calling start() from Car:
Inside self of Derived
Car class
'''