#Schedule multiple tasks one to print "Lunch Time!" at 1 PM & another to print "Wrap up work"
# at 6 PM.

import schedule
import time

def Display1():
    print("Lunch Time!")

def Display2():
    print("Wrap up work")

def main():
    print("Scheduling every day at 1:00 PM & 6:00 PM: ")

    schedule.every().day.at("13:00").do(Display1)
    schedule.every().day.at("18:00").do(Display2)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

