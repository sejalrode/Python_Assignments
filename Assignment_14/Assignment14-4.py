'''Create a class Student with name,rollno & a class variable school_name.print student details
& school name.Change the school name using class name.'''

class Student:
    school_name = "Marvellous"

    def __init__(self,sname,srollno):
        self.name = sname
        self.rollno = srollno

    def Display(self):
        print("Student Name : ",self.name)
        print("Student rollno : ",self.rollno)
        print("School name : ",Student.school_name)
        
def main():
    sobj1 = Student("Amit",11)
    sobj2 = Student("Smita",21)

    print("Before changing school name:")
    sobj1.Display()
    sobj2.Display()

    Student.school_name = "Infosystems"

    print("\nAfter changing school name:")
    sobj1.Display()
    sobj2.Display()
    
if __name__ == "__main__":
    main()

'''

'''