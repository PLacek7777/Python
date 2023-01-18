import threading
import socket
import time

PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

HEADER = 64
FORMAT = "utf-8"
DISCONECT_COMADN = "?disconect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn, addr):
    t = time.strftime("%H:%M:%S", time.localtime())
    print(f'[SERVER : {t}]>> New conection: {addr}')
    conected = True
    while conected:
        msgLeangt = conn.recv(HEADER).decode(FORMAT)
        if msgLeangt:
            msgLeangt = int(msgLeangt)
            msg = conn.recv(msgLeangt).decode(FORMAT)
            if str.lower(msg) == "?disconect":
                conected = False
            t = time.strftime("%H:%M:%S", time.localtime())
            print(f'[{addr} : {t}]>> {msg}')
            conn.send("Recvd".encode(FORMAT))
    
    conn.close()
    t = time.strftime("%H:%M:%S", time.localtime())
    print(f"[SERVER : {t}]>> {addr}: disconected")
    print(f'[SERVER : {t}]>> Active conections: {threading.active_count()-2}')

def start():
    server.listen()
    t = time.strftime("%H:%M:%S", time.localtime())
    print(f"[SERVER : {t}]>> Server started!")
    print(f'[SERVER : {t}]>> IPv4: {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
        t = time.strftime("%H:%M:%S", time.localtime())
        print(f'[SERVER : {t}]>> Active conections: {threading.active_count()-1}')

t = time.strftime("%H:%M:%S", time.localtime())
print(f"[SERVER : {t}]>> Server is starting...")
start()