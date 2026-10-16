import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 9999))
print("Listening on port 9999...")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Got from {addr}: {data.decode()}")