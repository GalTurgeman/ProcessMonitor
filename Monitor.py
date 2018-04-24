'''
Created on 16 Apr 2018

@author: gal
'''
import psutil
from Process import MyProcess
from time import sleep, localtime,strftime

file1 = open('/Users/gal/Desktop/old.csv','w')#First Sample
file2 = open('/Users/gal/Desktop/new.csv','w')#Second Sample

List1 = []
List2 = []

while True:
    pl = psutil.pids()
#     print "First Loop"
    for p in range (0,len(pl)):
        temp = MyProcess()
        try:
            temp.Process(psutil.Process(pl[p]))
        except psutil.NoSuchProcess:
            pass
        List1.append(temp)
        file1.write(temp.getPid()+","+temp.getName()+","+temp.getCTime()+","+temp.getStatus())
        file1.write("\r\n")
        with open("/Users/gal/Desktop/Process_List_File.csv", "a") as Process_List_File: #All Samples!
            Process_List_File.write(temp.getPid()+","+temp.getName()+","+temp.getCTime()+","+temp.getStatus())
            Process_List_File.write("\r\n")
    sleep(2)
    pl = psutil.pids()
#     print "Second Loop"
    for p in range (0,len(pl)):
        temp = MyProcess()
        try:
            temp.Process(psutil.Process(pl[p]))
        except psutil.NoSuchProcess:
            pass
        List2.append(temp)
        file2.write(temp.getPid()+","+temp.getName()+","+temp.getCTime()+","+temp.getStatus())
        file2.write("\r\n")
        with open("/Users/gal/Desktop/Process_List_File.csv", "a") as Process_List_File: #All Samples!
            Process_List_File.write(temp.getPid()+","+temp.getName()+","+temp.getCTime()+","+temp.getStatus())
            Process_List_File.write("\r\n")   
    for l in List1:
        if l not in List2:
#             print "Closed Loop"
            print l.getName()+","+l.getPid()+","+l.getCTime()+","+"Closed"+","+"Time: "+strftime("%X ", localtime())
            with open("/Users/gal/Desktop/Status_Log_File.csv", "a") as Status_Log_File: #Changes!
                Status_Log_File.write(l.getName()+","+l.getPid()+","+l.getCTime()+","+"Closed")
                Status_Log_File.write("\r\n")
    for q in List2:
        if q not in List1:
#             print "Opened Loop"
            print q.getName()+","+q.getPid()+","+q.getCTime()+","+"Closed"+","+"Time: "+strftime("%X ", localtime())
            with open("/Users/gal/Desktop/Status_Log_File.csv", "a") as Status_Log_File: #Changes!
                Status_Log_File.writelines (q.getName()+","+q.getPid()+","+q.getCTime()+","+"Opened")
                Status_Log_File.write("\r\n")
