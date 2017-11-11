import threading
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM

SIZE = 1024

PORT = 6000
PORT1 = 5000

IP = gethostbyname('192.168.1.101')
IP1 = gethostbyname('0.0.0.0')
mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket1 = socket(AF_INET, SOCK_DGRAM)

mySocket1.bind((IP1, PORT1))

mySocket.connect((IP, PORT))

name = input("enter you name : ")


def chatIN():
    while (True):
        print('')
        (data,addr) = mySocket1.recvfrom(SIZE)
        data = data.decode()
        (name, data) = data.split(':')
        print(name + " : " + data)

thread2 = threading.Thread(target=chatIN)
thread2.start()


def chatOUT():
    while (True):
        print('')
        data = input()
        if data == 'exit(0)':
            data = name + ':<' + name + ' has left the chat >'
            mySocket.sendto(data.encode('utf-8'), (IP, PORT))
            break
        data = name + ':' + data
        mySocket.sendto(data.encode('utf-8'), (IP, PORT))
thread1 = threading.Thread(target=chatOUT)
thread1.start()
