import socket
import threading
import csv
import os
#opening connections
u = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
u.bind((socket.gethostbyname(socket.gethostname()), 1224))
def key_in(c,a):
    #declaring variables
    name = ""
    lock = ""
    #recive key setup message
    msg = c.recv(1024)
    msgr = msg.decode("utf-8")
    #name finding
    for i in msgr:
            if i != "[":
                name += i
            else:
                break
    #key finding
    for i in msgr[len(name)+1:]:
        if i != "~":
            lock +=i
        else:
            print lock
            #add in key to spred sheet
            with open("public_keys.csv","a") as key_public:
                key_public = csv.writer(key_public)
                key_public.writerow([name] + [lock])
    with open("ports.csv","a") as ports:
        ports = csv.writer(ports)
        find = True
        with open("ports.csv","r+") as portsr:
            portsr = csv.reader(portsr)
            #port reserving
            for row_number, row in enumerate(portsr):
                port = row[1]
                if row[0] == name:
                    find = False
            if find:
                print int(port)+1
                ports.writerow([name]+[int(port)+1])
#listening for connections
while True:
    u.listen(1000000)
    clientsocket, address = u.accept()
    pro = threading.Thread(target=key_in, args=[clientsocket, address])
    pro.start()
