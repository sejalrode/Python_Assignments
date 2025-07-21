'''Create 3 threads named as small,capital & digit.All thread will accept string as parameter.
Small thread will display no of small characters,capital thread no of capital characters &
Digit thread no of digit.Display id and name of each thread.'''

import threading

def SmallChar(String):
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID of Small is : ",threading.get_ident())
    count = 0
    for i in String:
        if(i >= 'a' and i <= 'z'):
            count = count + 1
    print("Count of small characters : ",count)

def CapitalChar(String):
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID of Capital is : ",threading.get_ident())
    count = 0
    for i in String:
        if(i >= 'A' and i <= 'Z'):
            count = count + 1
    print("Count of capital characters : ",count)

def DigitNo(String):
    print("Thread Name:", threading.current_thread().name)
    print("Thread ID of Digit is : ",threading.get_ident())
    count = 0
    for i in String:
        if(i >= '0' and i <= '9'):
            count = count + 1
    print("Count of digit : ",count)

def main():
    Input = input("Enter a string : ")

    print("Thread Name:", threading.current_thread().name)
    print("Thread ID of main is : ",threading.get_ident())

    Small = threading.Thread(target = SmallChar,args = (Input,))
    Capital = threading.Thread(target = CapitalChar,args = (Input,))
    Digit = threading.Thread(target = DigitNo,args = (Input,))

    Small.start()
    Capital.start()
    Digit.start()

if __name__ == "__main__":
    main()

'''
Enter a string : sejal RODE 0415

Thread Name: MainThread
Thread ID of main is :  13284

Thread Name: Thread-1 (SmallChar)
Thread ID of Small is :  3344
Count of small characters :  5

Thread Name: Thread-2 (CapitalChar)
Thread ID of Capital is :  1508
Count of capital characters :  4

Thread Name: Thread-3 (DigitNo)
Thread ID of Digit is :  10236
Count of digit :  4
'''