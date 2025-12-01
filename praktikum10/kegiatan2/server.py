import socket
import platform

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)

print("Server siap...")
c, a = s.accept()
print("Terhubung:", a)

while True:
    perintah = c.recv(1024).decode().lower()

    if perintah == "machine":
        c.send(platform.machine().encode())

    elif perintah == "release":
        c.send(platform.release().encode())

    elif perintah == "system":
        c.send(platform.system().encode())

    elif perintah == "version":
        c.send(platform.version().encode())

    elif perintah == "node":
        c.send(platform.node().encode())

    elif perintah == "quit":
        c.send("bye".encode())
        break

    else:
        c.send("unknown command".encode())

c.close()
s.close()
