'''Create 2 threads named as thread1 & thread2.thread1 will display 1 to 50 & thread2 
will display 50 to 1.After execution of thread1 gets completed then schedule thread2'''

import threading

def Display():
    for i in range(1,51):
        print("thread1 : ",i)

def Reverse():
    for i in range(50,0,-1):
        print("thread2 : ",i)

def main():
    
    Thread1 = threading.Thread(target = Display)
    Thread2 = threading.Thread(target = Reverse)

    Thread1.start()
    Thread1.join()

    Thread2.start()

if __name__ == "__main__":
    main()

'''
thread1 :  1
thread1 :  2
thread1 :  3
thread1 :  4
thread1 :  5
thread1 :  6
thread1 :  7
thread1 :  8
thread1 :  9
thread1 :  10
thread1 :  11
thread1 :  12
thread1 :  13
thread1 :  14
thread1 :  15
thread1 :  16
thread1 :  17
thread1 :  18
thread1 :  19
thread1 :  20
thread1 :  21
thread1 :  22
thread1 :  23
thread1 :  24
thread1 :  25
thread1 :  26
thread1 :  27
thread1 :  28
thread1 :  29
thread1 :  30
thread1 :  31
thread1 :  32
thread1 :  33
thread1 :  34
thread1 :  35
thread1 :  36
thread1 :  37
thread1 :  38
thread1 :  39
thread1 :  40
thread1 :  41
thread1 :  42
thread1 :  43
thread1 :  44
thread1 :  45
thread1 :  46
thread1 :  47
thread1 :  48
thread1 :  49
thread1 :  50
thread2 :  50
thread2 :  49
thread2 :  48
thread2 :  47
thread2 :  46
thread2 :  45
thread2 :  44
thread2 :  43
thread2 :  42
thread2 :  41
thread2 :  40
thread2 :  39
thread2 :  38
thread2 :  37
thread2 :  36
thread2 :  35
thread2 :  34
thread2 :  33
thread2 :  32
thread2 :  31
thread2 :  30
thread2 :  29
thread2 :  28
thread2 :  27
thread2 :  26
thread2 :  25
thread2 :  24
thread2 :  23
thread2 :  22
thread2 :  21
thread2 :  20
thread2 :  19
thread2 :  18
thread2 :  17
thread2 :  16
thread2 :  15
thread2 :  14
thread2 :  13
thread2 :  12
thread2 :  11
thread2 :  10
thread2 :  9
thread2 :  8
thread2 :  7
thread2 :  6
thread2 :  5
thread2 :  4
thread2 :  3
thread2 :  2
thread2 :  1
'''