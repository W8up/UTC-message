import socket
import RSA
import csv
import getpass
import threading
#declaring variables
p = 3
d = 0
n = 0
real = ""
private = ""
encry = RSA.change()
def connection(c,a,private,text,n,d):
    encry = RSA.change()
    #connection from server
    print ("Connection from " + str(a) + " has been established")

    #sectioning message
    
    msg = ""
    last_msg = ""
    #checking that message is not repeated
    while True:
        p = 1
        real = ""
        msg = c.recv(1024)
        if msg != "":
            rmsg = msg.decode("utf-8")
            print rmsg
            real = encry.decrypt(rmsg, d, n)
            last_msg = msg


#getting username and key
name = str(getpass.getuser())
try:
    f = open(name + "Key.txt","r")
except:
    #key generation
    run = RSA.keygen()
#locating exsisting key
f = open(name + "Key.txt","r")
text = str(f.readlines())
f.close()
#connecting to address update
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.connect((socket.gethostbyname(socket.gethostname()), 1223))
a.send(bytes(name))
port = a.recv(1024)
portr = int(port.decode("utf-8"))
print portr
a.close()
print text
for i in range(len(text)):
    if text[i] == "]":
        private = text[3:i]
        print private
        break
        

#seperating ecryption parts
for i in range(len(private)):
    if str(private[i]) == " ":
        d = int(private[:int(i-1)])
        n = int(private[int(i+1):])
        print n
        print d


#opening communication channel
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()), portr))
while True:
    s.listen(1000000)
    clientsocket, address = s.accept()
    pro = threading.Thread(target=connection, args=[clientsocket, address, private, text,n,d])
    pro.start()
    

