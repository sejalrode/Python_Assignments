'''Compare execution time of summing numbers from 1 to 10 million using normal function,
threading and multiprocessing.'''

import threading
import multiprocessing
import time

def SumNo(No):
    Sum = 0
    for i in range(No+1):
        Sum = Sum + i
    return Sum
    
def main():
    start_time = time.time()
    ret = SumNo(10000000)
    print("Sum : ",ret)
    end_time = time.time()
    print("Time required for normal function is : ",end_time - start_time)
    
    start_time = time.time()
    t1 = threading.Thread(target = SumNo, args = (10000000,))
    t1.start()
    print("Sum : ",ret)
    end_time = time.time()
    print("Time required for threading is : ",end_time - start_time)

    start_time = time.time()
    P1 = multiprocessing.Process(target = SumNo, args = (10000000,))
    P1.start()
    print("Sum : ",ret)
    end_time = time.time()
    print("Time required for multiprocessing is : ",end_time - start_time)


if __name__ == "__main__":
    main()

'''
Sum :  50000005000000
Time required for normal function is :  0.7339644432067871

Sum :  50000005000000
Time required for threading is :  0.01693248748779297

Sum :  50000005000000
Time required for multiprocessing is :  0.5938735008239746
'''