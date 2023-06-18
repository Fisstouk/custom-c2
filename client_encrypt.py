from port_scanner import get_network_address
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

# Get network address from the function
net_address = get_network_address()

# Convert to strings
string_address = str(net_address)

# Convert it to bytes
bytes_address = bytes(string_address, encoding='utf-8')

try:
    wrappedSocket.sendall(bytes_address)
    # wrappedSocket.sendall(b'Hello')
    data = wrappedSocket.recv(4096)
finally:
    print("Received", data)
    wrappedSocket.close()
