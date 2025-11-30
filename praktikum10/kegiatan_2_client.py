import socket

c = socket.socket()
c.connect(("localhost", 5000))

print("Program komunikasi tentang server")

while True:
    p = input("Command: ")
    c.send(p.encode())

    respon = c.recv(1024).decode()
    print("Response:", respon)

    if p.lower() == "quit":
        break

c.close()
