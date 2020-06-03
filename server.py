import socket

def receive():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 8080))
    s.listen(2)
    conn, addr = s.accept()
    print("accepted")
    print(bytes.decode(conn.recv(1024)))



if __name__ == "__main__":

    receive()
