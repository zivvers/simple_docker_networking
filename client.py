import socket






if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    command = "bridge test!"
    print("connecting...")
    sock.connect( ('172.16.238.1', 8080) )
    print("sending!")
    sock.sendall(command.encode())
