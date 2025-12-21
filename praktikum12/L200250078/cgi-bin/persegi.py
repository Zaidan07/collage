def hitung_luas(sisi):
    """fungsi menghitung luas persegi"""
    return sisi * sisi

print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print("<html>")
print("<head><title>Bangun Geometri</title></head>")
print("<body style='display: flex; justify-content: center; align-items: center;'>")

sisi = 10
luas = hitung_luas(sisi)

print("<h2 style='text-align: center;'>Bangun Geometri</h2>")
print("<table border='1' cellpadding='5'>")
print("<tr><td>Nama bangun</td><td>: Persegi</td></tr>")
print("<tr><td>Dimensi</td><td>: 2D</td></tr>")
print("<tr><td>Rumus luas</td><td>: sisi x sisi</td></tr>")
print(f"<tr><td>Parameter</td><td>: sisi = {sisi}</td></tr>")
print(f"<tr><td>Luas</td><td>: {luas}</td></tr>")
print("</table>")

print("</body>")
print("</html>")
