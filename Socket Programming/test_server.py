print("??")
import socket
from urllib import response
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
HOST = "127.0.0.1"
PORT = 65432


def handlePostRequest():
    return

def handleGetRequest(filename):
    print(filename.replace("/", ""))
    try:
        fin = open("d:/8th Term/Networks/Socket Programming/"+filename.replace("/", ""))
        content = fin.read()
        fin.close()
        response = 'HTTP/1.0 200 OK\n\n' + content
    except (FileNotFoundError, IOError):   
        response = "HTTP/1.0 404 Not Found\r\n" 
    return response 

def parseRequest(req):
    headers = req.split('\n')
    requestType = headers[0].split()[0]
    print(requestType)
    filename = headers[0].split()[1]
    print(filename)
    if (requestType == 'GET'):
       content = handleGetRequest(filename)
    #TO BE USED LATER   
    httpVersion = headers[0].split()[2]

    return content

server_address = (HOST,PORT)

while True:
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind(server_address)
        s.listen()
        print("The server is ready to recieve...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                req = conn.recv(1024)
                if not req:
                    break
                response = parseRequest(req.decode())

                conn.sendall(response.encode())
            
