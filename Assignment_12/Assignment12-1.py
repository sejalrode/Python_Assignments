class Demo:

    def __init__(self,value1,value2):
        self.no1 = value1
        self.no2 = value2

    def Fun(self):
        print("Fun no1 : ",self.no1)
        print("Fun no2 : ",self.no2)

    def Gun(self):
        print("Gun no1 : ",self.no1)
        print("Gun no2 : ",self.no2)

def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()

'''
Fun no1 :  11
Fun no2 :  21
Fun no1 :  51
Fun no2 :  101
Gun no1 :  11
Gun no2 :  21
Gun no1 :  51
Gun no2 :  101
'''