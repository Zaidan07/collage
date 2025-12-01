import socket

data = {
    "nama": "Muhammad Zaidan Nabih",
    "nim": "L200250078",
    "angkatan": "2025"
}

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)

print("Server siap...")
c, a = s.accept()   
print("Terhubung dengan : ", a)

while True :
    perintah = c.recv(1024).decode().lower()
    
    if perintah in data:
        c.send(data[perintah].encode())
    elif perintah == "keluar":
        c.send("siap!".encode())
        break
    else:
        c.send("Maaf, perintah tidak dimenegrti".encode())
        
c.close()
s.close()