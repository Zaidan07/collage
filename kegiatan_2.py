import random

num = random.randint(100, 700)


## Program Akun
## Dibuat oleh Muhammad Zaidan Nabih L200250078
Nama = "Muhammad Zaidan Nabih"
TanggalLahir = "08 Oktober 2006"
NamaSingkat = Nama[0] + "." + "Zaidan" + "." + Nama[-5]
UserName= Nama[0] + TanggalLahir[0:2] + TanggalLahir[11:16]
Password = Nama[0:3] + str(num)

print(f"Nama : {Nama}")
print(f"Tanggal Lahir : {TanggalLahir}")
print(f"Nama Singkat : {NamaSingkat}")
print(f"User Name : {UserName}")
print(f"Password : {Password}")