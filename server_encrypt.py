import socket
import ssl

# Create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 12345))
sock.listen(1)

# Wrap socket in SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

while True:
    print("Waiting for connection...")
    conn, addr = sock.accept()

    # Wrap incoming ocnnection in a SSL context
    connssl = context.wrap_socket(conn, server_side=True)

    try:
        print("Connected by", addr)
        while True:
            data = connssl.recv(1024)
            if not data:
                break
            print("Received", data)
            connssl.sendall(data)
    finally:
        connssl.shutdown(socket.SHUT_RDWR)
        connssl.close()
