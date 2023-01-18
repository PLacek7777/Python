import socket

PORT = 5555
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONECT_COMADN = "?disconect"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msgLeanght = len(message)
    sendLenght = str(msgLeanght).encode(FORMAT)
    sendLenght += b' ' * (HEADER - len(sendLenght))
    client.send(sendLenght)
    client.send(message)
    print("[SERVER]>> " + client.recv(2048).decode(FORMAT))

print("[CONSLOE]>> To quit type 'q' in input")

while True:
    inp = input("[INPUT]>> ")
    if inp == 'q':
        send(DISCONECT_COMADN)
        break
    else:
        send(inp)