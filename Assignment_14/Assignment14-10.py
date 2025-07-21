'''Demonstrate private,protected & public access modifiers using a class Employee with 
attributes : __salary,_department,name.'''

class Employee:
    def __init__(self,ename,edepartment,esalary):
        self.name = ename                   #public
        self._department = edepartment      #protected
        self.__salary = esalary             #private

    def Display(self):
        print("Employee name : "+self.name)
        print("Employee department : "+self._department)
        print("Employee salary : ",self.__salary)
        
 
def main():

    eobj = Employee("Amit","Development",50000)

    eobj.Display()

    print(eobj.name)
    print(eobj._department)
    #print(eobj.__salary) 

if __name__ == "__main__":
    main()

'''

'''

