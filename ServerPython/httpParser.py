import util as u

class HTTP_Parser:

    def __init__(self):
        self.body = ""
        self.code = 0

    def ParseHttpRequest(this,request: bytes):
        '''
        request comes from what the client
        sent to the server
        '''

        data = request.decode().splitlines()[0].split(' ')
        file = File()

        print("------------------------------------")
        print(f"[DEBUG] HTTP method: {data[0]}")
        print(f"[DEBUG] path: {data[1]}")

        if data[0] == 'GET':
            if data[1] == '/test400':
                this.body = file.openFile("/templates/400.html")
                this.code = 400
            elif data[1] == '/':
                this.body = file.openFile("/templates/index.html")
                if this.body:
                    this.code = 200
                else:
                    this.body = file.openFile("/templates/404.html")
                    this.code = 404
            else:
                this.body = file.openFile("/templates" + data[1])
                if this.body:
                    this.code = 200
                else:
                    this.body = file.openFile("/templates/404.html")
                    this.code = 404

    def createHeaders(this):

        response = ""

        match this.code:
            case 200:
                response += u.HTTP_CODE_200
            case 400:
                response += u.HTTP_CODE_400
            case 404:
                response += u.HTTP_CODE_404

        response += u.CRLF
        response += f"Content-Type: text/html; charset=utf-8{u.CRLF}"
        response += f"Content-Length: {len(this.body.encode('utf-8'))}{u.CRLF}"
        response += f"Connection: close{u.CRLF}"
        response += u.END_HEADERS
        response += this.body

        return response.encode("utf-8")
        
class File:
    def openFile(self, path):
        try:
            with open("." + path,'r') as f:
                return f.read()
        except OSError:
            print("[ERROR - SERVER] File dont exist")
            return None
