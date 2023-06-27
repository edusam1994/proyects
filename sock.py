import socket
hostname = socket.gethostname()
ip= socket.gethostbyname(hostname)


print("name of your desktop is :"+ hostname)
print("Your IP adress is :"+ ip)