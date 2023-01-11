import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sock.connect(("www.youtube.com", 443))
sock.sendto(b"GET / HTTP/3\r\nHost:www.example.com\r\n\r\n",
            ("www.youtube.com", 443))
response = sock.recv(4096)
print(response)
print(response.decode())

sock.close()
