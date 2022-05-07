print("??")
import socket
from urllib import response

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "127.0.0.1"
PORT = 65432

from _thread import *
import threading

print_lock = threading.Lock()

def handlePostRequest(headers,filename):
    content = headers[0].split()[-1]
    response = 'HTTP/1.0 200 OK\n\n' + content
    print(response)
    fin = open("d:/8th Term/Networks/Socket Programming/"+filename.replace("/", ""),"w+")
    content = fin.write("This is a test2 file \n use this as a test \nfor the server")
    fin.close()
    return response

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
    elif  (requestType == 'POST'):
       content = handlePostRequest(headers,filename)
    #TO BE USED LATER   
    httpVersion = headers[0].split()[2]

    return content

def threaded(c):
    while True:
 
        # data received from client
        data = c.recv(1024)
        
        if not data:
            print('Connection closed')
             
            # lock released on exit
            print_lock.release()
            break
        response = parseRequest(data.decode('utf-8'))
        c.sendall(response.encode('utf-8'))
    # connection closed
    c.close()
     
def Main():
    server_address = (HOST,PORT)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.bind(server_address)
    s.listen()
    print("The server is ready to recieve...")

    while True:  

        conn, addr = s.accept()
        #is used to change state to locked
        print_lock.acquire()
        start_new_thread(threaded, (conn,))

    s.close()




if __name__ == '__main__':
    Main()

            
