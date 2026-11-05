#############################################################################
#
#   Importing required libraries
#
#############################################################################
import os
import sys
import time
import schedule
import psutil

#############################################################################
#
#   Function name:      ProcessDisplay
#   Input:              None
#   Description:        Fetches the information of currently running processes.
#   Date:               05/11/2026
#   Author:             Shivam Ramesh Kurlekar
#
#############################################################################
def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            # Fetch process details
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            # Memory usage in MB
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            listprocess.append(pinfo)
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
            
    return listprocess

#############################################################################
#
#   Function name:      ProcessLog
#   Input:              FolderName (string)
#   Description:        Creates a timestamped log file containing process 
#                       details in the specified directory.
#   Date:               05/11/2026
#   Author:             Shivam Ramesh Kurlekar
#
#############################################################################
def ProcessLog(FolderName):
    Border = "-" * 50

    # Create destination directory if it doesn't exist
    if not os.path.exists(FolderName):
        try:
            os.mkdir(FolderName)
            print(f"Directory '{FolderName}' created successfully.")
        except Exception as e:
            print(f"Error creating directory: {e}")
            return
            
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    LogFileName = os.path.join(FolderName, "ProcessLog_%s.log" % timestamp)

    try:
        fobj = open(LogFileName, "w")
        print(f"Log file created: {LogFileName}")

        fobj.write(Border + "\n")
        fobj.write("---- Automated Process Logger System (Core Monitor) ----\n")
        fobj.write("Log generated at: " + timestamp + "\n")
        fobj.write(Border + "\n")
        
        listprocess = ProcessDisplay()
        
        for element in listprocess:
            fobj.write(f"PID: {element['pid']} | Name: {element['name']} | User: {element['username']} | RAM: {element['vms']:.2f} MB\n")
            
        fobj.write(Border + "\n")
        fobj.write("------------------ End of log file ---------------------\n")
        
        fobj.close()
        print("Process logging completed successfully.")
        print(Border)
        
    except Exception as e:
        print(f"Error writing to log file: {e}")

#############################################################################
#
#   Function name:      main
#   Input:              None
#   Description:        Entry point of the script, handles command line 
#                       arguments and scheduling loop.
#   Date:               05/11/2026
#   Author:             Shivam Ramesh Kurlekar
#
#############################################################################
def main():
    Border = "-" * 50
    print(Border)
    print("---- Core Monitor ----")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1].lower() in ["--h", "-h"]:
            print("This automation script is used to perform:")
            print("1: Fetching information of all running processes.")
            print("2: Generating timestamp-based log files periodically.")
            print("3: Managing log directories automatically.")
            
        elif sys.argv[1].lower() in ["--u", "-u"]:
            print("Use the automation script as: ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution.")
            print("Folder_Name   : Directory where logs will be stored.")
            
        else:
            print("Unable to proceed as there is no matching argument.")
            print("Please use --h or --u flag for getting more details.")

    elif len(sys.argv) == 3:
        try:
            interval = int(sys.argv[1])
            folder_name = sys.argv[2]
            
            print("Scheduler started successfully.")
            print(f"Generating process logs in '{folder_name}' every {interval} minute(s).")
            print("Press Ctrl + C to abort.")
            print(Border)
            
            # Initial run so you don't wait for the first interval
            ProcessLog(folder_name)
            
            schedule.every(interval).minutes.do(ProcessLog, folder_name)
            
            while True:
                schedule.run_pending()
                time.sleep(1)
                
        except ValueError:
            print("Error: Time_Interval must be an integer.")
            
    else:
        print("Invalid number of arguments.")
        print("Please use --h or --u flag for getting more details.")

    print(Border)
    print("--- Thank you for using the Core Monitor ---")
    print(Border)

#############################################################################
#
#   Starter of main
#
#############################################################################

if __name__ == "__main__":
    main()