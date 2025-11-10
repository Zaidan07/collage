nama = input("Masukkan nama : ")
waktu = float(input("Masukkan waktu : "))

jam = int(waktu)

if 1 <= jam <= 10:
    ucapan = "Selamat pagi"
elif 11 <= jam <= 14:
    ucapan = "Selamat siang"
elif 15 <= jam <= 17:
    ucapan = "Selamat sore"
else:
    ucapan = "Selamat malam"

print(f"{ucapan} {nama}.")
