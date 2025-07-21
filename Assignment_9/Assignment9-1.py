'''Start 3 threads each printing numbers from 1 to 5 with a delay of 1 second.'''

import threading
import time

def Display():
    for i in range(1,6):
        print(f"{threading.current_thread().name} : {i}")
        time.sleep(1)

def main():
    
    t1 = threading.Thread(target = Display, name = 'Thread1')
    t2 = threading.Thread(target = Display, name = 'Thread2')
    t3 = threading.Thread(target = Display, name = 'Thread3')

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()

'''
Thread1 : 1
Thread2 : 1
Thread3 : 1
Thread1 : 2
Thread2 : 2
Thread3 : 2
Thread1 : 3
Thread2 : 3
Thread3 : 3
Thread2 : 4
Thread1 : 4
Thread3 : 4
Thread1 : 5
Thread2 : 5
Thread3 : 5
'''