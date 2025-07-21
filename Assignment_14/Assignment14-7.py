'''Create a base class Person with name & age.Derive a class Teacher with subject & salary.
Use super() to call base class constructor & print both.'''

class Person:

    def __init__(self,pname,page):
        self.name = pname
        self.age = page
    
    def Display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
    
class Teacher(Person):

    def __init__(self,pname,page,tsubject,tsalary):
        super().__init__(pname,page)
        self.subject = tsubject
        self.salary = tsalary

    def Display(self):
        super().Display()
        print("Subject : ",self.subject)
        print("Salary : ",self.salary)
        
def main():
    tobj1 = Teacher("Amit",35,"Math",35000)
    tobj2 = Teacher("Smita",42,"Science",55000)

    tobj1.Display()
    tobj2.Display()
    
if __name__ == "__main__":
    main()

'''
Name :  Amit
Age :  35
Subject :  Math
Salary :  35000

Name :  Smita
Age :  42
Subject :  Science
Salary :  55000
'''