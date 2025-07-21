#Script that simulates checking for email updates every 10 seconds.
#(Use a print statement like "Checking mail..." instead of real mail logic.)

import schedule
import time

def MailChecking():
    print("Checking mail...")

def main():
    print("Scheduling Mail checking: ")

    schedule.every(10).seconds.do(MailChecking)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

'''
Scheduling Mail checking:
Checking mail...
Checking mail...
'''