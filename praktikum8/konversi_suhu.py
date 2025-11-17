def konversiSuhu(C=None, F=None):
    if C is not None:
        Fh = (9/5) * C + 32
        print(f"Suhu {C} Celcius setara dengan {Fh} Fahrenheit")
        return Fh
    
    elif F is not None:
        Cl = (5/9) * (F - 32)
        print(f"Suhu {F} Fahrenheit setara dengan {Cl} Celcius")
        return Cl
    
    else:
        C = 0
        Fh = (9/5) * C + 32
        print(f"Suhu {C} Celcius setara dengan {Fh} Fahrenheit")
        return Fh
    
    
    
    
# Cara kerja singkat:
# - Jika C tidak None → hitung Fahrenheit
# - Jika F tidak None → hitung Celcius
# - Jika keduanya None → pakai C = 0 (default)
# - None dipakai untuk mengecek apakah parameter diberikan