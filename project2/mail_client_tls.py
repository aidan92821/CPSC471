# Aidan Williams
# Brandon Cobb
# Joshua Germing

from socket import *
import ssl
import base64
import os

# Configuration - Using environment variables for security
GMAIL_USERNAME = os.getenv('GMAIL_USER', 'sender@gmail.com')  
GMAIL_PASSWORD = os.getenv('GMAIL_PASS', 'password')     
RECIPIENT_EMAIL = os.getenv('RECIPIENT', 'receiver@gmail.com')  

# Message content
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose Gmail server
mailserver = "smtp.gmail.com"
port = 587  # Gmail TLS port

print("Connecting to Gmail SMTP server...")

# Create socket and establish TCP connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))

# Initial server response
recv = clientSocket.recv(1024).decode()
print("Server:", recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
    exit()

# Send HELO command
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("Server:", recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    exit()

# Send STARTTLS command to initiate TLS encryption
print("Initiating TLS connection...")
starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv_tls = clientSocket.recv(1024).decode()
print("Server:", recv_tls)
if recv_tls[:3] != '220':
    print('220 reply not received for STARTTLS.')
    exit()

# Wrap socket with TLS/SSL
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)
print("TLS connection established.")

# Send HELO again after TLS (required)
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv_helo2 = clientSocket.recv(1024).decode()
print("Server:", recv_helo2)

# Authenticate with Gmail using AUTH LOGIN
print("Authenticating...")
authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv_auth = clientSocket.recv(1024).decode()
print("Server:", recv_auth)

# Send base64 encoded username
username_b64 = base64.b64encode(GMAIL_USERNAME.encode()).decode()
clientSocket.send((username_b64 + '\r\n').encode())
recv_user = clientSocket.recv(1024).decode()
print("Server:", recv_user)

# Send base64 encoded password
password_b64 = base64.b64encode(GMAIL_PASSWORD.encode()).decode()
clientSocket.send((password_b64 + '\r\n').encode())
recv_pass = clientSocket.recv(1024).decode()
print("Server:", recv_pass)
if recv_pass[:3] != '235':
    print('Authentication failed.')
    exit()
print("Authentication successful!")

# Send MAIL FROM command
mailFromCommand = f'MAIL FROM:<{GMAIL_USERNAME}>\r\n'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print("Server:", recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
    exit()

# Send RCPT TO command
rcptToCommand = f'RCPT TO:<{RECIPIENT_EMAIL}>\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print("Server:", recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
    exit()

# Send DATA command
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print("Server:", recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')
    exit()

# Send email headers and message
email_content = f"""From: {GMAIL_USERNAME}
To: {RECIPIENT_EMAIL}
Subject: Test Email from SMTP Client with TLS

{msg.strip()}
"""

clientSocket.send(email_content.encode())

# End message with period
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print("Server:", recv5)
if recv5[:3] != '250':
    print('Email sending failed.')
else:
    print('Email sent successfully!')

# Send QUIT command
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print("Server:", recv6)

# Close connection
clientSocket.close()
print("Connection closed.")