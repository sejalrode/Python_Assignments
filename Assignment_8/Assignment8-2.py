'''Create 2 threads named as evenfactor & oddfactor.Both thread will accept one parameter as 
an integer.EvenFactor thread will display addition of even factors of given number same for
OddFactor.After execution of both the threads gets completed main thread should display msg 
as "exit from main". '''

import threading

def EvenFactor(value):
    Sum = 0
    for i in range(2,value+1):
        if((value % i == 0) and (i % 2 == 0)):
            Sum = Sum + i
    print("Even Factors Sum : ",Sum)

def OddFactor(value):
    Sum = 0
    for i in range(1,value+1):
        if((value % i == 0) and (i % 2 != 0)):
            Sum = Sum + i
    print("Odd Factors Sum : ",Sum)

def main():
    No = int(input("Enter a number : "))

    Even = threading.Thread(target = EvenFactor,args = (No,))
    Odd = threading.Thread(target = OddFactor,args = (No,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

'''
Enter a number : 4
Even Factors Sum :  6
Odd Factors Sum :  1
Exit from main
'''