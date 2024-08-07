from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while True:
    payload, clientAddress = serverSocket.recvfrom(2048)
    message = payload.decode()
    print(f'RECEIVED: {clientAddress} => {message}')
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
