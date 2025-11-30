import random

# Fungsi untuk membaca file item
def load_items(nama_file):
    try:
        with open(nama_file, "r") as file:
            return [item.strip() for item in file.readlines() if item.strip()]
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan!")
        return []

def simpan_riwayat(teks):
    with open("riwayat_gacha.txt", "a") as file:
        file.write(teks + "\n")

def gacha():
    print("\n=== Sistem Gacha (3 Item Sekaligus) ===")

    # Load item dari file
    common = load_items("common.txt")
    rare = load_items("rare.txt")
    epic = load_items("epic.txt")
    legendary = load_items("legendary.txt")

    # 3 kali roll
    for i in range(3):
        roll = random.randint(1, 100)

        if roll <= 50:
            item = random.choice(common)
            rarity = "Common"
        elif roll <= 80:
            item = random.choice(rare)
            rarity = "Rare"
        elif roll <= 95:
            item = random.choice(epic)
            rarity = "Epic"
        else:
            item = random.choice(legendary)
            rarity = "Legendary"

        hasil = f"[{rarity}] {item}"
        print(f"({i+1}) Anda mendapatkan: {hasil}")
        simpan_riwayat(hasil)

def main():
    print("Selamat datang di Sistem Gacha!")

    while True:
        input("\nTekan ENTER untuk gacha 3x...")
        gacha()

        lagi = input("\nIngin gacha lagi? (y/n): ")
        if lagi.lower() != 'y':
            print("\nTerima kasih sudah bermain!")
            print("Riwayat gacha tersimpan di: riwayat_gacha.txt")
            break

main()
