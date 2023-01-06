import socket
from _thread import *
import sys

server = "192.168.1.151"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(2)
print("SERVER STARTED")
print("Listening, you can conect")

def client(self):
    
    conn.send(str.encode("Conected"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            
            if not data:
                print("Disconected...")
                break
            else:
                print("RECV>> ", reply)
                print("SEND>> ", reply)

            conn.sendall(str.encode(reply))
        except:
            print("ERROR")
            print("BREAKING")
            break
    print("conection lost")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Conection accepted")
    print(f'>> {addr} <<')

    start_new_thread(client, (conn, ))
