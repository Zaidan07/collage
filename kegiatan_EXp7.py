# import time
# from datetime import datetime

# while True:
#     sekarang = datetime.now()
#     jam = sekarang.strftime("%H:%M:%S")
#     print(jam)

#     if sekarang.second == 0:
#         print("Jam praktikum sudah habis. Silakan pulang.")
#         break

#     time.sleep(1)


import time
from datetime import datetime

mulai_jam = 8
mulai_menit = 10

akhir_jam = 9
akhir_menit = 50

while True:
    sekarang = datetime.now()

    jam = sekarang.hour
    menit = sekarang.minute
    detik = sekarang.second

    print(sekarang.strftime("%H:%M:%S"))

    if jam == akhir_jam and menit == akhir_menit and detik == 0:
        print("Jam praktikum sudah habis. Silakan pulang.")
        break

    time.sleep(1)

