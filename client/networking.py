import socket

class Network:
    def __init__(self):
        self.HEADER = 64
        self.server = "IP"
        self.port = "PORT"
        self.FORMAT = "utf-8"
        self.DISCONNECT_MSG = "!disconnect"
        self.ADDR = (self.server, self.port)

    def set_ip(self, ip, port):
        self.server = ip
        self.port = port
        self.ADDR = (self.server, self.port)

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self, msg):
        self.message_s = msg.encode(self.FORMAT)
        self.msg_lenght_s = len(msg)
        self.send_lenght_s = str(self.msg_lenght_s).encode(self.FORMAT)
        self.send_lenght_s += b' ' * (self.HEADER - len(self.send_lenght_s))
        self.client.send(self.send_lenght_s)
        self.client.send(self.message_s)

    def disconnect(self):
        self.send(self.DISCONNECT_MSG)

    def recv(self):
        self.msg_lenght_r = self.client.recv(self.HEADER).decode(self.FORMAT)
        self.msg_lenght_r = int(self.msg_lenght_r)
        self.msg_r = self.client.recv(self.msg_lenght_r).decode(self.FORMAT)
