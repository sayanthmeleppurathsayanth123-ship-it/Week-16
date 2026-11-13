import socket

c=socket.socket()

c.connect(('localhost', 9999))
print("connected to server")

while True:
    msg=input("you: ")
    if msg.strip()=="":
        continue
    if msg.lower()== "exit":
        break
        #send message to server
    c.sendall(msg.encode())

    #receivng response from server
    data= c.recv(1024).decode()

    if not data:
        print("server disconnected")
        break
    print("server:", data)

c.close()