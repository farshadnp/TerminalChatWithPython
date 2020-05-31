import time, socket, sys
 
print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)
 
s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1234
print("\nTalash Baraye Connect Shodan ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Vasl Shode...\n")
 
s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "be chatroom ezafe shod\nEnter [e] to exit chat room\n")
 
while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("man : "))
    if message == "[e]":
        message = "Left chat room!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())