import random
import csv
import time
global real
import socket
import RSA
import getpass
real = ""
class keygen:
    def __init__(self):
        #find prime numbers
        primeList = []
        max = 5000
        for x in range(2, max + 1):
            isPrime = True
            for y in range(2, int(x**0.5)+1):
                if x % y == 0:
                    isPrime = False
                    break
            if isPrime:
                primeList.append(x)

        p = primeList[random.randint(15,len(primeList))]
        q = primeList[random.randint(25,len(primeList))]
        #RSA encryption
        n = p * q
        while p == q or n >= 5000000:
            q = primeList[random.randint(25,len(primeList))]
            q = primeList[random.randint(25,len(primeList))]
            n = p * q
        on = (p-1)*(q-1)
        e = random.randrange(1, on)
        g = gcd(e, on)
        #checks validility
        while g != 1:
            e = random.randrange(1, on)
            g = gcd(e, on)
        lock = [e, n]
        ec = e+1
        while True:
            d = ((on * ec) + 1) / float(e)
            if float(d).is_integer():
                key = [int(d), n]
                d = int(d)
                break
            ec +=1

        time.sleep(2)
        name = str(getpass.getuser())
        #connects to key update
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostbyname(socket.gethostname()), 1224))
        s.send(bytes(name + "["+ str(lock)+"~"))
        s.close()
        f = open(name + "key.txt", "a")
        f.writelines(str(key))
        f.close()
def gcd(a, b):
    #finds gcd
    while b != 0:
        a, b = b, a % b
    return a

class change:
    def encrypt(self, msg, e, n):
        #encryption
        en = "1"
        ph = 0
        for char in msg:
            if ord(char) < 100:
                if ord(char) < 10:
                    en = str(en)+ "00"+str(ord(char))
                else:
                    en = str(en)+ "0" + str(ord(char))
            else:
                en = str(en)+ str(ord(char))
            ph = int(en)    
        en = int((ph ** e) % n)
        return en
    def decrypt(self, char, d, n):
        #decryption
        real =""
        msg = ""
        try:
            for i in char:
                if i != "]":
                    if i == ",":
                        de = ""
                        ph2 = 0
                        ph = ""
                        ph2 = int((int(msg) ** int(d)) % int(n))
                        c = 1
                        for i in str(ph2)[1:]:
                            if c < 3:
                                ph += str(i)
                                c += 1
                            else:
                                ph += str(i)
                                if ph[0] != "0":
                                    de += chr(int(ph))
                                    ph = ""
                                    c = 1
                                else:
                                    de += chr(int(str(ph)[1:]))
                                    ph = ""
                                    c = 1
                        msg = ""
                        real += str(de)
                    else:
                        msg += i
                else:
                    f = open("Chat.txt","a")
                    f.writelines(str(real)+"\n")
                    f.close()
                    print real
                    real = ""
        except:
            return None
