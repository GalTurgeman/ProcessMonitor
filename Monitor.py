
import psutil,time,base64,datetime,os,platform
from time import strftime,localtime,sleep
 

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        print ("Incorrect data format, should be YYYY-MM-DD HH:MM:SS")
        main()
    
def MonitorMode(x):
    try:
        print('Start Scanning\n______________________________________________________________________')
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
                        print (str(key) + "," + name + "," +  "opened" + "," +strftime("%Y-%m-%d %H:%M:%S", localtime()))
                        status_log.write(base64.b64encode(str(key) + "," + name + "," +  "opened" + "," +strftime("%Y-%m-%d %H:%M:%S", localtime())))
                        status_log.write("\r\n")
            value = {k: dict1[k] for k in set(dict1) - set(dict2)}
            if (value):
                for key, value1 in value.items():
                    with open("Status_Log_File.csv", "a") as status_log:
                        name, status, time = value1
                        print (str(key) + "," + name + "," +  "closed" + "," +strftime("%Y-%m-%d %H:%M:%S", localtime()))
                        status_log.write(base64.b64encode(str(key) + "," + name + "," +  "closed" + "," +strftime("%Y-%m-%d %H:%M:%S", localtime())))
                        status_log.write("\r\n")
    except KeyboardInterrupt:
        print ("\n Back to main!\n")
        main()
            
def DecodeMode():
    try:
        with open("process_list.csv") as process_list:
            process_list_Decode = open("process_list_Decode.csv","a")
            l=process_list.readlines()
            for i in l: 
                process_list_Decode.write(base64.b64decode(i))
                process_list_Decode.write("\r\n")
    except IOError:
        print ("There is no encode file for processList!\n")
        pass
    try:
        with open("Status_Log_File.csv") as Status_Log_File:
            Status_Log_File_Decode = open("Status_Log_File_Decode.csv","a")
            l=Status_Log_File.readlines()
            for i in l: 
                Status_Log_File_Decode.write(base64.b64decode(i))
                Status_Log_File_Decode.write("\r\n")
    except IOError:
        print ("There is no encode file for Status_Log!\n")
        pass
    try:
        with open("Status_Log_File_Manual.csv") as Status_Log_File:
            Status_Log_File_Decode = open("Status_Log_File_Manual_Decode.csv","w+")
            l=Status_Log_File.readlines()
            for i in l: 
                Status_Log_File_Decode.write(base64.b64decode(i))
                Status_Log_File_Decode.write("\r\n")
    except IOError:
        print ("There is no encode file for Status_Log_File_Manual!\n")
    
        
def ManualMonitor():
    user_input1 = raw_input("Enter First time in format  YYYY-MM-DD HH:MM:SS\nExample:2018-04-29 21:39:46 \n")
    validate(user_input1)
    user_input2 = raw_input("Enter Second time same format: \n")
    validate(user_input2)
    dict1={}
    dict2={}

    with open("process_list_Decode.csv") as f:
        for line in f:
            if user_input1 in line:
                s= line.split(",")
                dict1[s[0]] = s[1] #dict[pid] = process_name
    with open("process_list_Decode.csv") as f:            
        for line in f:
            if user_input2 in line:
                s= line.split(",")
                dict2[s[0]] = s[1] #dict[pid] = process_name
#     print dict1
#     print dict2
    value = {k: dict2[k] for k in set(dict2) - set(dict1)}
    if (value):
        with open("Status_Log_File_Manual.csv", "w+") as status_log:
            for key, value1 in value.items():
                status_log.write("\r\n")
                name = value1
                print (str(key) + "," + name + "," +  "opened")
                status_log.write(base64.b64encode(str(key) + "," + name + "," +  "opened"))
                    
    value = {k: dict1[k] for k in set(dict1) - set(dict2)}
    if (value):
        with open("Status_Log_File_Manual.csv", "w+") as status_log:
            for key, value1 in value.items():
                status_log.write("\r\n")
                name = value1
                print (str(key) + "," + name + "," +  "closed")
                status_log.write(base64.b64encode(str(key) + "," + name + "," +  "closed"))
                
def readNumber(x):
    try:
        return int(x) # raw_input in Python 2.x
    except ValueError:
        pass
      
def isItExit(x):
    if(x=="exit()"):
        return True
    else:
#         raise ValueError('A very specific bad thing happened.')
        pass
    
def Auth(user,password):
    mine = base64.b64encode(password)
    mine2 = base64.b64encode(user)
    if(mine2 =="QWRtaW4=" and mine == "UHIwMGNlNTVNMG4hNzBS"):
        print ("Success!")
    return mine2 =="QWRtaW4=" and mine == "UHIwMGNlNTVNMG4hNzBS"
def DeleteFiles():
    if platform.system() == "Windows":
        os.system("del *.csv")
    else:
        os.system("rm *.csv")
     
def main():
    print ("-----------Process Monitor-----------")
    counter = 0
    try:
        user = raw_input("Enter user name:\n")
        password = raw_input("Enter password:\n")
        if not Auth(user, password):
            while(counter < 3):
                print "Wrong username or password, try again. "
                print Auth(user, password)
                counter+=1
                user = raw_input("Enter user name:\n")
                password = raw_input("Enter password:\n")
                if(counter == 2):
                    print "Too much tries, bye-bye!"
                    if(platform.system()=="Windows"):
                        os.system("type Bye.txt")
                    else:
                        os.system("cat Bye.txt") 
                    exit()
                if(Auth(user, password)):
                    counter = 4
    except KeyboardInterrupt:
        if(platform.system()=="Windows"):
            os.system("type Bye.txt")
        else:
            os.system("cat Bye.txt") 
        exit()
    while(True):
        try:
            if(platform.system()=="Windows"):
                os.system("cls")
                os.system("type art.txt")
            else:
                os.system("clear")
                os.system("cat art.txt")
            x = raw_input("(*)For Monitor Mode press 1 \n(*)For Decode Mode press 2 \n(*)For Manual Mode press 3\n(*)Delete all files press 4\n(*)For quit exit() or ctr+c\n")
            if (readNumber(x)):
                if(int(x) == 1):
                    sec = raw_input("Enter interval in seconds: \n")
                    MonitorMode(int(sec)) 
                    continue 
                elif(int(x) == 2):
                    DecodeMode()
                elif(int(x) == 3):
                    ManualMonitor()
                elif(int(x) == 4):
                    DeleteFiles()
                else:
                    print "Invalid input, try again!"
            elif (isItExit(x)):
                exit()
            else:
                print "Invalid input, try again!"
        except KeyboardInterrupt:
            print ("\n Bye Bye!\n")
            if(platform.system()=="Windows"):
                os.system("type Bye.txt")
            else:
                os.system("cat Bye.txt") 
            exit()           
        
if __name__ == '__main__':
    main()

