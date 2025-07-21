#Schedule a function that performs file backup every hour & writes a log entry into backup_log.txt.

import schedule
import time
import os
import sys

def CreateLog(Fname):
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(":","_")
    timestamp = timestamp.replace("/","_")

    FileName = "backup_log%s.log" %(timestamp)
    
    fobj = open(FileName, "w")

    border = "-"*80
    fobj.write(border)
    fobj.write("\n\t\tMarvellous Infosystems Backup Log\n")
    fobj.write("\t\tLog file is created at : "+time.ctime()+"\n")
    fobj.write(border)

    Data = FileBackup(Fname)

    fobj.write("%s \n\n" %Data)

    fobj.write("\n"+border)

    fobj.close()


def FileBackup(filename):
    flag = os.path.exists(filename)

    if(flag == False):
        print("No such file")
        exit()

    fobj = open(filename,"r")

    data = fobj.read()

    fobj.close()

    return data

def main():
    print("Scheduling file backup every hour: ")

    if len(sys.argv) != 2:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")
        return

    if (sys.argv[1] == "--h") or (sys.argv[1] == "--H"):
        print("This application is used to perform file backup")
        print("This is the automation script")
        return

    elif (sys.argv[1] == "--u") or (sys.argv[1] == "--U"):
        print("Use the given script as :")
        print("python script_name.py <filename>")
        print("Please provide valid absolute path")
        return

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print("The file does not exist. Please check the path.")
        return

    schedule.every(1).minutes.do(lambda: CreateLog(filename))

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

