import socket

s=socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('localhost', 9999))

s.listen(3)

print("server is listening")
c, addr= s.accept()
print("connected with ", addr)

while True:
    data= c.recv(1024).decode()

    if not data:
        print("client disconnected")
        break
    print("client :", data )

    reply=input("server reply:")
    c.sendall(reply.encode())

c.close()
s.close()