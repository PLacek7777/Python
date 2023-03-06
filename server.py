from configparser import ConfigParser
import threading
import logging
import socket

# Logging setup
logging.basicConfig(filename="Server.log", level=logging.DEBUG, format='%(asctime)s >> %(message)s')

# Config file setup
conf = ConfigParser()
conf.read("conf.config")
confData = conf["CONF"]

# Constants from config file
PORT = int(confData["SERVER_PORT"])
SERVER = confData["SERVER_ADRESS"]
ADDR = (SERVER, PORT)
NAME_HEADER = int(confData["NAME_HEADER"])
FORMAT = confData["FORMAT"]

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Client thread
def handleClient(conn, addr):
    name = conn.recv(NAME_HEADER).decode(FORMAT)
    logging.info(f'Connected: {addr[0]}: {name}')
    while True: 
        try: 
            check = conn.recv(1)
        except:
            conn.close()
            logging.info(f'Disconnected: {addr[0]}: {name}')
            break
# Server thread (main thread)
def start():
    server.listen()
    logging.info("Started")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn, addr))
        thread.start()
# Server startup
start()