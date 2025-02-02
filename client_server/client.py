import os
import socket

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.client_socket.connect((self.ip, self.port))
        print(self.client_socket.recv(1024).decode())
        self.init_response()
    
    def init_response(self):
        operation = str(input("Do you want to Download or Upload a file?")).lower()
        self.client_socket.send(operation.encode())
        if operation == "upload":
            file_name = str(input("Which file do you wish to upload?"))
            self.upload_file(file_name)
        elif operation == "download":
            self.download_file()
        else:
            print("Invalid input, please try again")
            self.init_response()



    def upload_file(self,file_name):
        self.client_socket.send(file_name.encode())
        file = open(file_name, "rb")
        data = file.read()
        self.client_socket.sendall(data)
        self.client_socket.send(b"<END>")

    def download_file(self):
        # path = str(input("Where do you want to save the file:"))
        print(self.client_socket.recv(1024).decode())
        path = "C:/Users/Shalev/.vscode/Main/client_server/file_download/"
        file_name = str(input(""))
        self.client_socket.send(file_name.encode())
        file = open((f"{path}{file_name}"), "wb")
        bytes_file = b""
        finished = False
        while not finished:
            data = self.client_socket.recv(1024)
            if data[-5:] == "<END>".encode():
                bytes_file += data
                finished = True
            else:
                bytes_file += data
        file.write(bytes_file[:-5])
        file.close()
        

my_client = Client('127.0.0.1', 1234)
my_client.connect_to_server()
