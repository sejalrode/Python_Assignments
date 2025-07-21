'''Create 2 threads named as even & odd.Even thread will display first 10 even numbers & odd
thread will display first 10 odd numbers.'''

import threading

def EvenNo():
    for i in range(2,21,2):
        print("Even numbers : ",i)

def OddNo():
    for i in range(1,20,2):
        print("Odd numbers : ",i)

def main():
    
    Even = threading.Thread(target = EvenNo)
    Odd = threading.Thread(target = OddNo)

    Even.start()
    Odd.start()

if __name__ == "__main__":
    main()

'''
Even numbers :  2
Even numbers :  4
Even numbers :  6
Even numbers :  8
Odd numbers :  1
Even numbers :  10
Even numbers :  12
Even numbers :  14
Even numbers :  16
Even numbers :  18
Even numbers :  20
Odd numbers :  3
Odd numbers :  5
Odd numbers :  7
Odd numbers :  9
Odd numbers :  11
Odd numbers :  13
Odd numbers :  15
Odd numbers :  17
Odd numbers :  19
'''