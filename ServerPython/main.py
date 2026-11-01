from server import Server
from httpParser import HTTP_Parser

def main():
    serv = Server("0.0.0.0",8080)
    parser = HTTP_Parser()
    conn, addr = serv.start()
    request = serv.HandleConnection(conn, addr, 4096)
    parser.ParseHttpRequest(request)
    h = parser.createHeaders()
    conn.sendall(h)
    conn.close()
main()