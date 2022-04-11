import socket
import threading
import csv
import os
#socket opening
u = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
u.bind((socket.gethostbyname(socket.gethostname()), 1223))
def ip_update(c,a):
    msg = c.recv(1024)
    name = msg.decode("utf-8")
    try:
        #ip finding
        with open("ips_temp.csv", "w") as out_file:
            with open("ips.csv", "r") as in_file:
                in_csv = csv.reader(in_file)
                out_csv = csv.writer(out_file)
                for row_number, row in enumerate(in_csv):
                    if str(row[0]) != name:
                        out_csv.writerow([row[0]]+[row[1]])
                in_file.close()
            out_file.close()
        os.remove("ips.csv")
        with open("ips.csv", "a") as in_file:
            with open("ips_temp.csv", "r") as out_file:
                in_csv = csv.writer(in_file)
                out_csv = csv.reader(out_file)
                try:
                    for row in enumerate(out_csv):
                        in_csv.writerow([row[1][0]]+[row[1][1]])
                    in_csv.writerow([name]+[a])
                except:
                    in_csv.writerow([name]+[a])
                in_file.close()
            out_file.close()
        os.remove("ips_temp.csv")
    except:
        #ip file creation
        with open("ips.csv", "a") as in_file:
            in_csv = csv.writer(in_file)
            in_csv.writerow([name]+[a])
        in_file.close()
    #port finding and relay
    with open("ports.csv","a") as ports:
        ports = csv.writer(ports)
        find = True
        with open("ports.csv","r+") as ports:
            ports = csv.reader(ports)
            for row in enumerate(ports):
                print row[1][0]
                print row[1][1]
                if str(row[1][0]) == str(name):
                    port = row[1][1]
                    print port
                    c.send(bytes(port))
                    find = False
            if find:
                print int(port)+1
                ports.writerow([name]+[int(port)+1])
                c.send(bytes(int(port)+1))
            

    c.close()
#listening for new connections
while True:
    u.listen(1000000)
    clientsocket, address = u.accept()
    pro = threading.Thread(target=ip_update, args=[clientsocket, address])
    pro.start()
