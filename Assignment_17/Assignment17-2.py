#Display current date & time every minute using the datetime module

import schedule
import time
import datetime

def Display():
    print("Current date & time : ",datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

'''
Current date & time :  2025-06-16 23:19:06.777263
Current date & time :  2025-06-16 23:20:06.822269
Current date & time :  2025-06-16 23:21:06.867411
'''