import os
import socket

class Server:
    def __init__(self, port):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket type TCP 
        # not typing IP so the server can listen to requests coming from other computers on the network
        self.server_socket.bind(('', port))

    def start_listen(self):
        while True:
            self.server_socket.listen(5)
            client, addr = self.server_socket.accept()
            client.send(("I'm Listening Mate").encode())
            self.init_response(client)
        self.server_socket.close()

    def init_response(self, client):
        operation = client.recv(1024).decode()
        if operation == "upload":
            self.receive_file(client)
        elif operation == "download":
            self.transfer_file(client)

    def receive_file(self, client):
        file_name = client.recv(1024).decode()
        file = open(f'C:/Users/Shalev/.vscode/Main/client_server/file_upload/{file_name}', "wb")
        bytes_file = b""
        finished = False
        while not finished:
            data = client.recv(1024)
            if data[-5:] == "<END>".encode():
                bytes_file += data
                finished = True
            else:
                bytes_file += data
        file.write(bytes_file)
        file.close()

    def transfer_file(self, client):
        client.send((f"input your chosen file: {os.listdir('C:/Users/Shalev/.vscode/Main/client_server/file_upload/')}").encode())
        file_name = (client.recv(1024)).decode()
        file = open(f"C:/Users/Shalev/.vscode/Main/client_server/file_upload/{file_name}", "rb")
        data = file.read()
        client.sendall(data)
        client.send(b"<END>")

my_server = Server(1234)
my_server.start_listen()