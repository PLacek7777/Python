from configparser import ConfigParser
import threading
import logging
import socket

conf = ConfigParser()
conf.read("conf.config")
confData = conf["SERVER"]

PORT = int(confData["PORT"])
SERVER = ''
ADDR = (SERVER, PORT)

HEADER = int(confData["HEADER"])
FORMAT = confData["FORMAT"]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

logging.basicConfig(filename="Server.log", level=logging.DEBUG, format='%(asctime)s >> %(message)s')

def handleClient(conn, addr):
    while True:
        try:
            name = conn.recv(HEADER).decode(FORMAT)
            logging.info(f'Connected: {addr[0]}: {name}')
        except:
            conn.close()
            logging.info(f'Disconnected: {addr[0]}: {name}')
            break

def start():
    server.listen()
    logging.info("Started")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
start()