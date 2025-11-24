data_diri = {
    "NIM" : "L200250078",
    "Nama" : "Muhammad Zaidan Nabih",
    "Alamat" : "Tegalan, 02/04, Kateguhan, Tawangsari, Sukoharjo",
    "Program Studi" : "Teknik Informatika",
    "Fakultas" : "Komunikasi dan Informatika",
    "Hobi" : "Ngoding",
    "Kode Pos": "57875"
}

def tampil_nim():
    print("NIM", data_diri["NIM"])

def tampil_nama():
    print("Nama", data_diri["Nama"])
    
def tampil_alamat():
    print("Alamat", data_diri["Alamat"])
        
def tampil_program_studi():
    print("Program Studi", data_diri["Program Studi"])
    
def tampil_fakultas():
    print("Fakultas", data_diri["Fakultas"])
    
def tampil_hobi():
    print("Hobi", data_diri["Hobi"])
    
def tampil_kode_pos():
    print("Kode Pos", data_diri["Kode Pos"])


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

while pilihan != 'k':
    if pilihan == 'b':
        bantuan()
    elif pilihan == 'N':
        tampil_nim()
    elif pilihan == 'a':
        tampil_nama()
    elif pilihan == 'A':
        tampil_alamat()
    elif pilihan == 'p':
        tampil_program_studi()
    elif pilihan == 'f':
        tampil_fakultas()
    elif pilihan == 'h':
        tampil_hobi()
    elif pilihan == 'K':
        tampil_kode_pos()
    else:
        print("Perintah tidak dikenal!")

    pilihan = input("\nPilihan saudara: ")

print("Terima kasih.")