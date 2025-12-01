import socket

c = socket.socket()
c.connect(("localhost", 5000))

print("Menghitung luas persegi")

while True:
    p = input("Pesan : ")
    c.send(p.encode())

    jawaban = c.recv(1024).decode()
    print("Respon :", jawaban)

    if p.lower() == "keluar":
        break

c.close()
