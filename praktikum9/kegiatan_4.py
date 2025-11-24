import shelve

with shelve.open("Zaidan") as db:
    print("NIM           :", db["nim"])
    print("Tanggal lahir :", db["tanggal_lahir"])
    print("Nama lengkap  :", db["nama"])
    print("Kota          :", db["kota"])
