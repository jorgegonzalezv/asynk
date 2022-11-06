import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8888)
sock.connect(server_address)
try:
    # Send data
    message = b'This is the message.  It will be repeated.'
    print(type(message))
    print(message)
    sock.sendall(message)

finally:
    sock.close()
