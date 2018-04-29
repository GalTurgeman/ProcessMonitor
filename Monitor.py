
import psutil
import time
from time import strftime,localtime,sleep
import base64

    
def MonitorMode(x):
    try:
        print "Start Scanning\n______________________________________________________________________"
        while True:
            dict1 = {}
            for p in psutil.process_iter():
                dict1[p.pid] = p.name(), p.status(), p.create_time()
                with open("process_list.csv", "a") as process_list:
    #                 process_list.write(str(p.pid) + "," + p.name() + "," + strftime("%Y-%m-%d %H:%M:%S", localtime())+","+p.status())
    #                 process_list.write("\r\n")
                    process_list.write(base64.b64encode(str(p.pid) + "," + p.name() + "," + strftime("%Y-%m-%d %H:%M:%S", localtime())+","+p.status()))
                    process_list.write("\r\n")
            dict2 = {}
            sleep(x)
            for p in psutil.process_iter():
                dict2[p.pid] = p.name(), p.status(), p.create_time()
                with open("process_list.csv", "a") as process_list:
    #                 process_list.write(str(p.pid) + "," + p.name()+"," + strftime("%Y-%m-%d %H:%M:%S", localtime())+","+p.status() )
    #                 process_list.write("\r\n")
                    process_list.write(base64.b64encode(str(p.pid) + "," + p.name() + "," + strftime("%Y-%m-%d %H:%M:%S", localtime())+","+p.status()))
                    process_list.write("\r\n")
        
            value = {k: dict2[k] for k in set(dict2) - set(dict1)}
            if (value):
                for key, value1 in value.items():
                    with open("Status_Log_File.csv", "a") as status_log:
                        name, status, time = value1
                        print str(key) + "," + name + "," +  "opened" + "," +strftime("%Y-%m-%d %H:%M:%S", localtime())
                        status_log.write(base64.b64encode(str(key) + "," + name + "," +  "opened" + "," +strftime("%Y-%m-%d %H:%M:%S", localtime())))
                        status_log.write("\r\n")
            value = {k: dict1[k] for k in set(dict1) - set(dict2)}
            if (value):
                for key, value1 in value.items():
                    with open("Status_Log_File.csv", "a") as status_log:
                        name, status, time = value1
                        print str(key) + "," + name + "," +  "closed" + "," +strftime("%Y-%m-%d %H:%M:%S", localtime())
                        status_log.write(base64.b64encode(str(key) + "," + name + "," +  "closed" + "," +strftime("%Y-%m-%d %H:%M:%S", localtime())))
                        status_log.write("\r\n")
    except KeyboardInterrupt:
        print "\n Interrupted!\n"
            
def DecodeMode():
    try:
        with open("process_list.csv") as process_list:
            process_list_Decode = open("process_list_Decode.csv","a")
            l=process_list.readlines()
            for i in l: 
                process_list_Decode.write(base64.b64decode(i))
                process_list_Decode.write("\r\n")
    except OSError:
        print "\There is no encode file for processList!\n"
    try:
        with open("Status_Log_File.csv") as Status_Log_File:
            Status_Log_File_Decode = open("Status_Log_File_Decode.csv","a")
            l=Status_Log_File.readlines()
            for i in l: 
                Status_Log_File_Decode.write(base64.b64decode(i))
                Status_Log_File_Decode.write("\r\n")
    except OSError:
        print "\There is no encode file for Status_Log!\n"
        
def main():
    print "-----------Process Monitor-----------"
    try:
        x = input("For Monitor Mode press 1 | For decode Mode press 2  | regular Keyboard Interrupt for quit\n")
        if(x == 1):
            MonitorMode(5)  
        if(x == 2):
            DecodeMode()
    except KeyboardInterrupt:
        print "\n Interrupted!\n"            
        
if __name__ == '__main__':
    main()

