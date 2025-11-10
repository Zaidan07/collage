bangun = {
    "Segitiga": "L = 0.5 * a * t",
    "Persegi": "L = s * s",
    "Persegi Panjang": "L = p * l",
    "Lingkaran": "L = pi * r ** 2",
    "Jajaran Genjang": "L = a * t"
}

print("No | Nama Bangun       | Rumus Luas")
print("-------------------------------------")

no = 1
for nama, rumus in bangun.items():
    print(f"{no}  | {nama:<17} | {rumus}")
    no += 1
