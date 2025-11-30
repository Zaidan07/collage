import socket

c = socket.socket()
c.connect(("localhost", 5000))

print("Program komunikasi tentang data diri : ")

while True :
    p = input("Masukan perintah : ")
    c.send(p.encode())
    
    jawaban = c.recv(1024).decode()
    print("Jawab : ", jawaban)
    
    if p.lower() == "keluar":
        break

c.close()