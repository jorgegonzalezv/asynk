import socket

HOST = "127.0.0.1"
PORT = 8888 

# tcp socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind
socket.bind((HOST, PORT))

# listen for incoming connections
socket.listen(1)

while True:
    print("waiting...")
    connection, client_address = socket.accept()

    try:
        while True:
            data = connection.recv(16)
            print("recv: ", data)
            if not data:
                break
    finally:
        connection.close()

