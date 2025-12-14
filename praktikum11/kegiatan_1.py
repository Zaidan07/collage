import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap import Button

app = tk.Tk()
app.title("Data Diri")
app.geometry("800x400")
# app.configure(bg="#333333")
Style(theme="darkly")

card = tk.Frame(app, bg="#333333", padx=20, pady=20)
card.pack(padx=20, pady=20, fill="both")

tk.Label(card, text="Data Diri", font=("Segoe UI", 24, "bold"),
         bg="#333333", fg="white").pack(anchor="w", pady=(0, 10))

data = {
    "Nama": "Muhammad Zaidan Nabih",
    "NIM": "L200250078",
    "Buku favorit": "No Longer Human",
    "Idola": "Nabi Muhammad SAW",
    "Motto": "Tetaplah di jalan tuhan, walaupun kadang belok dikit"
}

for label, value in data.items():
    row = tk.Frame(card, bg="black")
    row.pack(anchor="w", pady=3)
    tk.Label(row, text=f"{label} :", font=("Segoe UI", 10, "bold"),
             fg="#555", bg="white").pack(side="left")
    tk.Label(row, text=value, font=("Segoe UI", 10),
             bg="white").pack(side="left")
    
    
# bagian iseng doang hehe
def open_new_window():
    new_window = tk.Toplevel(app)
    new_window.title("Secret Window")
    new_window.geometry("800x200")
    Style(theme="darkly")
    tk.Label(new_window, text="Hayolo, ngapain kamu open window ini?", font=("Segoe UI", 24, "bold"),
             bg="#333333", fg="white").pack(anchor="w", pady=(0, 10))

Button(
    app,
    text="Tutup",
    bootstyle="danger link",  
    command=app.quit,
    width=15
).pack(pady=5)

Button(
    app,
    text="Open Secret Window",
    bootstyle="danger link",  
    command=open_new_window,
    width=5
).pack(pady=5)

app.mainloop()
