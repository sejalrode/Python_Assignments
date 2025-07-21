class Employee:
    def __init__(self,ename,eid,esalary):
        self.name = ename
        self.id = eid
        self.salary = esalary

    def Display(self):
        print("Name : ",self.name)
        print("ID : ",self.id)
        print("Salary : ",self.salary)

def main():
    obj1 = Employee("Rohit",101,50000)
    obj2 = Employee("Amit",202,55000)

    obj1.Display()
    obj2.Display()

if __name__ == "__main__":
    main()

'''
Name :  Rohit
ID :  101
Salary :  50000

Name :  Amit
ID :  202
Salary :  55000
'''