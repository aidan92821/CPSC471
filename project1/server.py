# server.py

#import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 6789
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        # Read the HTTP request from the client
        message = connectionSocket.recv(1024).decode()

        # Parse out the requested filename
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket
        header = 'HTTP/1.1 200 OK\r\n'
        header += 'Content-Type: text/html\r\n'
        header += 'Connection: close\r\n'
        header += '\r\n'
        connectionSocket.send(header.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        header = 'HTTP/1.1 404 Not Found\r\n'
        header += 'Content-Type: text/html\r\n'
        header += 'Connection: close\r\n'
        header += '\r\n'
        body = '<html><body><h1>404 Not Found</h1></body></html>\r\n'

        connectionSocket.send(header.encode())
        connectionSocket.send(body.encode())
        connectionSocket.close()

# Close client socket
serverSocket.close()
sys.exit()
