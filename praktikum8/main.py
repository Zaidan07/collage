import datadiri as dd

def bantuan():
    print("Pilihan yang tersedia:")
    print("b menampilkan bantuan ini")
    print("N menampilkan NIM")
    print("a menampilkan Nama")
    print("A menampilkan Alamat")
    print("p menampilkan Program Studi")
    print("f menampilkan Fakultas")
    print("h menampilkan Hobi")
    print("K menampilkan Kode pos")
    print("k keluar")


bantuan()
pilihan = input("\nPilihan saudara: ")

while pilihan.lower() != 'k':
    if pilihan == 'b':
        bantuan()
    elif pilihan == 'N':
        dd.tampil_nim()
    elif pilihan == 'a':
        dd.tampil_nama()
    elif pilihan == 'A':
        dd.tampil_alamat()
    elif pilihan == 'p':
        dd.tampil_program_studi()
    elif pilihan == 'f':
        dd.tampil_fakultas()
    elif pilihan == 'h':
        dd.tampil_hobi()
    elif pilihan == 'K':
        dd.tampil_kode_pos()
    else:
        print("Perintah tidak dikenal!")

    pilihan = input("\nPilihan saudara: ")

print("Terima kasih.")