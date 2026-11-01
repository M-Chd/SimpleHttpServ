import socket
import httpParser as hp

class Server:

    port = 8080
    host = "0.0.0.0"

    def __init__(self,host,port):
        self.host = host
        self.port = port

    def start(this):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
            s.bind((this.host, this.port))
            s.listen()
            conn, addr = s.accept()
            return conn, addr

    def HandleConnection(this, conn, addr, buffer):
                print("-----------------------------------")
                print(f" > Connected by {addr}")
                data = conn.recv(buffer)
                if not data:
                    return None
                return data

    def printDebugSocketInfo(this):
        if this.socket:
            print("////////////////////////////////////////////////////////")
            print(f"[DEBUG - SERVER] Host: {socket.gethostname()}")
            print(f"[DEBUG - SERVER] Address Info: {socket.getaddrinfo(this.host,this.port)}")
            print("////////////////////////////////////////////////////////")

