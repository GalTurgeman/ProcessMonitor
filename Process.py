'''
Created on 13 Apr 2018

@author: gal
'''
import time

class MyProcess:
    myPid = 0
    myName =""
    myStatus =""
    myCTime = ""
    
    def __init__(self):
        self.myPid = ""
        self.myName = ""
        self.myStatus = ""
        self.myCTime = ""
        
    def Process(self,Process):
        self.myPid = str(Process.pid)
        self.myName = Process.name()
        self.myStatus = Process.status()
        self.myCTime = time.strftime('%d/%m/%Y %H:%M:%S',  time.gmtime(Process.create_time()))#for DD:MM:YY HH:MM:SS 
     
    def getPid(self):
        return self.myPid
    def getName(self):
        return self.myName
    def getStatus(self):
        return self.myStatus
    def getCTime(self):
        return self.myCTime
    
    def __eq__(self, other): 
        return self.getPid() == other.getPid()

    def setPid(self,PID):
        self.myPid = PID
    def setName(self,Name):
        self.myName = Name
    def setCTime(self,CTime):
        self.myCTime = CTime
    def setStatus(self,Status):
        self.myStatus = Status
    def toString(self):
        print "PID:",self.getPid(),"Name:",self.getName(),"Status:",self.getStatus(),"CTime:",self.getCTime()
    def __str__(self):
        return "PID: "+self.getPid()+" ,Name: "+self.getName()+" ,Status: "+self.getStatus()+" ,CTime: "+self.getCTime()