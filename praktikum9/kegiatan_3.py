import shelve

nama_file = "L200250078.txt"

with open(nama_file) as f:
    nim = f.readline().split(":")[1].strip()
    tgl = f.readline().split(":")[1].strip()
    nama = f.readline().split(":")[1].strip()
    kota = f.readline().split(":")[1].strip()

with shelve.open("Zaidan") as db:
    db["nim"] = nim
    db["tanggal_lahir"] = tgl
    db["nama"] = nama
    db["kota"] = kota

print("Data berhasil disimpan")
