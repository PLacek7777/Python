from configparser import ConfigParser
import socket
import time

conf = ConfigParser()
conf.read("conf.config")
confData = conf["CONF"]

PORT = int(confData["CLIENT_PORT"])
SERVER = confData["CLIENT_ADRESS"]
ADDR = (SERVER, PORT)
HEADER = int(confData["NAME_HEADER"])
FORMAT = confData["FORMAT"]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
message = (str(socket.gethostname())).encode(FORMAT)
msgLeanght = len(message)
message += b' ' * (HEADER - msgLeanght)
client.send(message)

while True:
    a = ''