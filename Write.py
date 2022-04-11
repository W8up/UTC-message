import RSA
import socket
import csv
#declaring variables
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname(socket.gethostname()), 1234))
e = 0
n = 0
d = 0
public = ""
private = ""
text = ""
#chose who to message
def chose(msg,name):
    #connection to server
    try:
        s.close()
    except:
        pass
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostbyname(socket.gethostname()), 1234))
    #request public key
    s.send(bytes(str(name)+"["))
    textr = s.recv(1024)
    text = textr.decode("utf-8")

    for i in range(len(text)):
        if text[i] == "]":
            public = text[0:i]
            break

    for i in range(len(public)):
        if str(public[i]) == " ":
            e = int(public[1:int(i-1)])
            n = int(public[int(i):])
            print e
            print n
    if len(msg) % 2 != 0:
        msg += " "
    #ecryption libary
    encry = RSA.change()
    c = 1
    ph = ""
    ph2 = 0
    msgts =""
    #chunks of two letters encrypted
    for i in msg:
        if c < 2:
            ph += i
            c += 1
        else:
            ph += i
            ph2 = int(encry.encrypt(ph, e, n))
            #validility check
            if int(ph2) < int(n):
                msgts += str(str(int(ph2))+",")
                ph = ""
                c = 1
            else:
                c = 2
    s.send(bytes(str(name)+str(msgts)+"]"))


