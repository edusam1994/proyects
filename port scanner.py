import sys
import socket

goal = input("Enter IP address to scan: ")

print("SCANNING GOAL: " + goal)

try:
    for port in range(1, 150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((goal, port))
        if result == 0:
            print("The port {} is open".format(port))
        s.close()

except Exception as e:
    print("\nAn error occurred:", str(e))
    sys.exit(0)
