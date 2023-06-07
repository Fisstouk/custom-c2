import socket
import ssl

# Create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap socket in SSL context
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

wrappedSocket = context.wrap_socket(sock, server_hostname='localhost')
wrappedSocket.connect(('localhost', 12345))

try:
    wrappedSocket.sendall(b"Hello!")
    data = wrappedSocket.recv(1024)
finally:
    print("Received", data)
    wrappedSocket.close()
