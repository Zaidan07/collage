Nama = "Muhammad Zaidan Nabih"
NIM = 1078
Tinggi = 1.7
Berat = 70
TahunLahir = 2006
Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
Data = [TahunLahir, Berat, Tinggi, NIM, Nama]

print(type(Aku))
print(Aku[0])

a = NIM % 4; Aku[a]
print(type(Aku[a]))
print(Aku[a:4])
print(type(Aku[4]))
# Aku[0] = "ok"

print(type(Data))
print(type(Data[4]))
print(Data[4][5])
print(Data[4][a:6])
Data[0] ="ok"; Data
print(Data[-a])
print(range(a))
