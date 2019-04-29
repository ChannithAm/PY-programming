import socket
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MSG = "Hello, World"

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = (UDP_IP, UDP_PORT)
print("Starting up on {0} port {1}".format(*server_address))
sock.bind(server_address)

while True:
    print("\nWaiting to receive message")
    data, address = sock.recvfrom(4096)

    print("Received {0} bytes from {1}".format(
        len(data), address
    ))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print("Sent {0} bytes back to {1}".format(
            sent, address
        ))