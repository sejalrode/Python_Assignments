#Program using multiprocessing.Pool to compute factorial of numbers in a list.

import multiprocessing

def Factorial(value):
    Fact = 1
    for i in range(1,value+1):
        Fact = Fact * i
    
    return Fact

def main():
    Data = []
    size = int(input("Enter number of elements : "))
    
    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    p = multiprocessing.Pool()  #Multicore
    result = p.map(Factorial,Data)

    p.close()
    p.join()
    
    print("Factorial : ",result)

if __name__ == "__main__":
    main()

'''
Enter number of elements : 2
Enter the elements :
4
5
Factorial :  [24, 120]
'''