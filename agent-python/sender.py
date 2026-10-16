import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b"hello argus", ("127.0.0.1", 9999))
print("Sent!")