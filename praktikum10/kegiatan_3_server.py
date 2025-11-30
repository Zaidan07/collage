import socket

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)

print("Server siap...")
c, a = s.accept()
print("Terhubung dengan : ", a)

sisi = 0   # tempat menyimpan parameter sisi persegi

while True:
    perintah = c.recv(1024).decode().lower()

    if perintah.startswith("param"):
        try:
            _, nilai = perintah.split()
            sisi = int(nilai)
            c.send("parameter dicatat".encode())
        except:
            c.send("format param salah".encode())

    elif perintah == "hitung":
        luas = sisi * sisi
        c.send(f"Luas persegi dengan sisi {sisi} adalah {luas}".encode())

    elif perintah == "keluar":
        c.send("-".encode())
        break

    else:
        c.send("Perintah tidak dimengerti".encode())

c.close()
s.close()
