import socket
import socketserver

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",65432)

# client_socket.sendto(b"Hello", server_address)
# print("[CLIENT] Done!")
# server_packet = client_socket.recvfrom(2048)
# print("[CLIENT] IN",server_packet)


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(server_address)
    message = "GET /4848 HTTP/1.0\nConnection: Keep-Alive\nUser-Agent: Mozilla/3.01 (X11; I; SunOS 5.4 sun4m)\nPragma: no-cache\nHost: tecfa.unige.ch:7778\nAccept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, */*"
    
    while True:
        s.send(message.encode('ascii'))
        data = s.recv(1024)
        print('Received from the server :',str(data.decode('ascii')))
 
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    s.close()