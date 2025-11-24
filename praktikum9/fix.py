import shelve

with shelve.open("Zaidan", writeback=True) as db:
    db["nim"] = "L200250078"
    db["tanggal_lahir"] = "10/08/2006"
    db["nama"] = "Muhammad Zaidan Nabih"
    db["kota"] = "Sukoharjo"

print("Shelve berhasil diperbaiki!")
