password_benar = "Zaidan"
kesempatan = 3

while kesempatan > 0:
    pwd = input("Masukkan password: ")

    if pwd == password_benar:
        print("Anda berhasil login.")
        break
    else:
        kesempatan -= 1
        print("Maaf, anda salah memasukkan password.")

        if kesempatan == 0:
            print("Anda telah mencoba 3 kali. Akses anda ditolak.")
