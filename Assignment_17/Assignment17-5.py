#Schedule a job that runs every 5 minutes to write current time to a file Marvellous.txt.

import schedule
import time
import datetime

def Display():
    fobj = open("Marvellous.txt","a")
    DateTime = datetime.datetime.now()
    fobj.write("Current date & time : "+str(DateTime)+"\n")

def main():
    schedule.every(3).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

'''

'''