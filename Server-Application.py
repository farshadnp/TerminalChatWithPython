# Client-Side App

import time,socket, sys

print("\nBe Chatroom Khosh Amadid.\n")
print("MeghdarDehiAvalie....\n")
time.sleep(1)
 
s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Lotfan Name Khod Ra Vared Konid: "))
           
s.listen(1)
print("\nDar Hale Entezar Baraye Peyda Kardan Client...\n")
conn, addr = s.accept()
print("Yek Etesal Az Address Roberoo Bargharar Shod ", addr[0], "(", addr[1], ")\n")
 
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "Vard ChatRoom Shod\nEnter [e] to exit chat room\n")
conn.send(name.encode())
 
while True:
    message = input(str("Man : "))
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)