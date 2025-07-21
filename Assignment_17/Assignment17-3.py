#Schedule a function to print "Do Coding...!" every 30 minutes.

import schedule
import time

def Display():
    print("Do Coding...!")

def main():
    print("Scheduling every 30 minutes : ")
    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

