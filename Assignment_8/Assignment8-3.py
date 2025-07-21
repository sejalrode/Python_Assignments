'''Create 2 threads named as evenlist & oddlist.Both thread will accept list of integers as 
parameter.EvenList thread will display addition of even no from given list same for
OddList. '''

import threading

def EvenList(values):
    Sum = 0
    for i in values:
        if(i % 2 == 0):
            Sum = Sum + i
    print("Even no Sum : ",Sum)

def OddList(values):
    Sum = 0
    for i in values:
        if(i % 2 != 0):
            Sum = Sum + i
    print("Odd no Sum : ",Sum)

def main():
    Data = []
    size = int(input("Enter the number of elements : "))

    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    Even = threading.Thread(target = EvenList,args = (Data,))
    Odd = threading.Thread(target = OddList,args = (Data,))

    Even.start()
    Odd.start()

if __name__ == "__main__":
    main()

'''
Enter the number of elements : 6
Enter the elements :
1
2
3
4
5
6
Even no Sum :  12
Odd no Sum :  9
'''