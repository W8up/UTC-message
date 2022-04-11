from Tkinter import *
import Write
global e
global n
import socket
import RSA
import csv
import getpass
import threading
import time
import os
try:
    os.remove("Chat.txt")
except:
    pass
e = 0
n = 0
root = Tk()
L1 = Label(root,text = "Name of recipient:")
L1.grid()
E1 = Entry(root)
E1.grid(column = 1,row = 0)
def read():
    import Read
pro = threading.Thread(target=read)
pro.start()
def connect():
    global e
    global n
    name = E1.get()
    msg = E2.get()
    n = Write.chose(msg,name)
def update():
    f = open("Chat.txt","a")
    f.close()
    f = open("Chat.txt","r")
    text = f.readlines()
    try:
        T1.delete("1.0",END)
    except:
        pass
    for i in text:
        T1.insert(END,str(i))
    f.close()
    root.after(2000,update)
L2 = Label(root,text = "Message:")
L2.grid(column = 0,row = 1)
E2 = Entry(root)
E2.grid(column = 1,row = 1)
B2 = Button(root, text = "Send", command = connect)
B2.grid(column = 2, row = 1)
T1 = Text(root,height = 20, width = 50)
T1.grid(row = 2)
T1.config(state=NORMAL)

root.after(2000,update)
root.mainloop()


