from Tkinter import *

import psutil,time,tkMessageBox as box
from time import strftime,localtime,sleep

# from test1 import MonitorMode
# import Tkinter as Tk

def MainWindow(bool):
    if(bool):
        Mwindow = Tk()
        Mwindow.title('Proceess Monitor')
        frame = Frame(Mwindow)
        btn = Button(frame, text = 'Start monitor mode',command = box.showinfo("GOOD","GOOD") )
        btn.pack(side = RIGHT , padx =5)
        frame.pack(padx=200,pady = 50)
        
def dialog1():
    username=entry1.get()
    password = entry2.get()
    if (username == 'admin' and  password == 'admin'):
        box.showinfo('info','Correct Login')
        MainWindow(True)
        window.destroy()
    else:
        box.showinfo('info','Invalid Login')

window = Tk()
window.title('Login')
frame = Frame(window)
Label1 = Label(window,text = 'Username:')
Label1.pack(padx=15,pady= 5)
entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)
Label2 = Label(window,text = 'Password: ')
Label2.pack(padx = 15,pady=6)
entry2 = Entry(window, bd=5)
entry2.pack(padx = 15,pady=7)
btn = Button(frame, text = 'Check Login',command = dialog1)
btn.pack(side = RIGHT , padx =5)
frame.pack(padx=200,pady = 50)
window.mainloop()

