import socket
import threading

HEADER = 64
PORT = 6969
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True

    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)

            msg = conn.recv(msg_lenght).decode(FORMAT)

            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()


def start():
    print(f"[Server] Listening on {SERVER}")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[INFO] Active Conns: " + str(threading.activeCount() -1))



print("[Starting] server is starting")
start()