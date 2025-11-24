nim = "L200250078"
tanggal_lahir = "08-10-2006"
nama = "Muhammad Zaidan Nabih"

nama_file = nim + ".txt"

with open(nama_file, "w") as f:
    f.write(f"NIM:{nim}\n")
    f.write(f"Tanggal Lahir:{tanggal_lahir}\n")   
    f.write(f"Nama:{nama}\n")
    
print("Berkas berhasil dibuat:",nama_file) 

# with open("L200250078.txt") as f:
#     baris = f.readlines()

# for i, b in enumerate(baris):
#     print(f"Baris {i}: {b!r}")
