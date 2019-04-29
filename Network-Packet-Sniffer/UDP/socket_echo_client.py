import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 5005)
msg = b'This is the message. It will be repeated.'

try:
    # Send data
    print('Sending {!r}'.format(msg))
    sent = sock.sendto(msg, server_address)

    # Receive response
    print("Waiting to receive")
    data, server = sock.recvfrom(4096)
    print("Received {!r}".format(data))

finally:
    print('Closing socket')
    sock.close()