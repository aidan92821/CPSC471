# client.py
import sys
from socket import *

def http_client(host, port, filename):
    # Create TCP socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Connect to the server
    clientSocket.connect((host, port))

    # Build and send the HTTP GET request
    request_line = f"GET /{filename} HTTP/1.1\r\n"
    headers = (
        f"Host: {host}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    http_request = request_line + headers
    clientSocket.send(http_request.encode())

    # Receive and print the response until the server closes
    response = b""
    while True:
        chunk = clientSocket.recv(4096)
        if not chunk:
            break
        response += chunk

    print(response.decode(errors='replace'))
    clientSocket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_host> <server_port> <filename>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]
    http_client(host, port, filename)
