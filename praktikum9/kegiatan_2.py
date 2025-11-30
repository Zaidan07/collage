nama_file = "L200250078.txt"

with open(nama_file) as f:
    lines = [line.strip() for line in f.readlines()]

nim = lines[0].split(":")[1]
tgl = lines[1].split(":")[1]
nama = lines[2].split(":")[1]

kota = "Sukoharjo"

hari, bulan, tahun = tgl.split("-")
tgl_baru = f"{bulan}/{hari}/{tahun}"

with open(nama_file, "w") as f:
    f.write(f"Nama:{nama}\n")  
    f.write(f"Kota:{kota}\n")
    f.write(f"Tanggal:{tgl_baru}\n")
    f.write(f"NIM:{nim}\n")     

with open(nama_file) as f:
    lines = [line.strip() for line in f.readlines()]

nama = lines[0].split(":")[1]
kota = lines[1].split(":")[1]
tgl_final = lines[2].split(":")[1]
nim_final = lines[3].split(":")[1]

print("Nama         :", nama)
print("Kota         :", kota)
print("Tanggal lahir:", tgl_final)
print("NIM          :", nim_final)
