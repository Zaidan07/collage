# def konversiSuhu(C=None, F=None):
#     if C is not None:
#         Fh = (9/5) * C + 32
#         print(f"Suhu {C} Celcius setara dengan {Fh} Fahrenheit")
#         return Fh
    
#     elif F is not None:
#         Cl = (5/9) * (F - 32)
#         print(f"Suhu {F} Fahrenheit setara dengan {Cl} Celcius")
#         return Cl
    
#     else:
#         C = 0
#         Fh = (9/5) * C + 32
#         print(f"Suhu {C} Celcius setara dengan {Fh} Fahrenheit")
#         return Fh

    

def konversiSuhu(C=None, F=None):
    
    if F is not None:
        print(f"Suhu {F} Farenheit setara dengan {(F-32)*5/9:.0f} Celcius")
    else:
        if C is None:
            C=0
        print(f"Suhu {C} Celcius setara dengan {(C*9/5)+32:.0f} Fahrenheit")
            

konversiSuhu(C=40)
konversiSuhu(F=95)
konversiSuhu(30)
konversiSuhu()