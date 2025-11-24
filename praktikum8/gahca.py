import random

def simpan_riwayat(teks):
    with open("riwayat_gacha.txt", "a") as file:
        file.write(teks + "\n")
        

def gacha():
    print("=== Sistem Gacha ===")
    print("1x Gacha akan memberikan satu item random.\n")
    
    roll = random.randint(1, 100)
    
    if roll <= 50:
        hasil = "Common Item"
    elif roll <= 80:
        hasil = "Rare Item"
    elif roll <= 95:
        hasil = "Epic Item"
    else:
        hasil = "Legendary Item"
        
    print(f"Selamat! Anda mendapatkan: {hasil}")
    simpan_riwayat(hasil)
    
def main():
    print("Selamat datang di Sistem Gacha!")
    
    while True:
        input("Tekan ENTER untuk gacha")
        gacha()
        
        lagi = input("Apakah Anda ingin melakukan gacha lagi? (y/n): ")
        if lagi.lower() != 'y':
            print("\nTerima kasih sudah bermain!")
            print("Riwayat gacha tersimpan di: riwayat_gacha.txt")
            break
        
        
main()