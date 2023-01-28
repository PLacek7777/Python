from configparser import ConfigParser
import socket
import time

conf = ConfigParser()
conf.read("conf.config")
confData = conf["SERVER"]

PORT = int(confData["PORT"])
SERVER = confData["SERVER"]
ADDR = (SERVER, PORT)
HEADER = int(confData["HEADER"])
FORMAT = confData["FORMAT"]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
    message = (str(socket.gethostname())).encode(FORMAT)
    msgLeanght = len(message)
    message += b' ' * (HEADER - msgLeanght)
    client.send(message)
    time.sleep(120)