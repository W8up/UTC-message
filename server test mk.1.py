import socket
import threading
import csv
#opening comunication ports
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.bind((socket.gethostbyname(socket.gethostname()), 1234))
def connection(c,a):
    #declariring variables
    name = ""
    text = ""
    lock = ""
    c_ips = ""
    c_ports = ""
    test = True
    test2 = True
    #reciving initilisation message
    msg = c.recv(1024)
    msgr = msg.decode("utf-8")
    #name grabing
    if test:
        for i in msgr:
            if i != "[":
                name += i
            else:
                test = False
                break
            #public key comunication
        with open("public_keys.csv","r") as public_keys:
            public_keys = csv.reader(public_keys)
            for row_number, row in enumerate(public_keys):
                if str(row[0]) == str(name):
                    text = str(row[1])
        c.send(bytes(str(text)))
    #incoming message relay
    #port finding
        with open("ports.csv","r") as ports:
            ports = csv.reader(ports)
            for row_number, row in enumerate(ports):
                if str(row[0]) == name:
                    c_port = int(row[1])
        # ip address finding
        with open("ips.csv","r") as ips:
            ips = csv.reader(ips)
            for row_number, row in enumerate(ips):
                if str(row[0]) == name:
                    c_ips = row[1]
    #outgoing connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((str(c_ips[2:-9]), c_port))
    while True:
        msg = c.recv(1024)
        if msg != None:
            msgr = msg.decode("utf-8")
            print msgr[len(name):]
            s.send(bytes(msgr[len(name):]))

#listening for incoming connection
while True:
    r.listen(1000000)
    clientsocket, address = r.accept()
    pro = threading.Thread(target=connection, args=[clientsocket, address])
    pro.start()
