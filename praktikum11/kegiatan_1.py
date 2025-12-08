import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap import Button

app = tk.Tk()
app.title("Data Diri")
app.geometry("800x400")
app.configure(bg="#f0f2f5")
Style(theme="flatly")

card = tk.Frame(app, bg="white", padx=20, pady=20,
                highlightthickness=1, highlightbackground="#d0d0d0")
card.pack(padx=20, pady=20, fill="both")

tk.Label(card, text="Data Diri", font=("Segoe UI", 24, "bold"),
         bg="white").pack(anchor="w", pady=(0, 10))

data = {
    "Nama": "Muhammad Zaidan Nabih",
    "NIM": "L200250078",
    "Buku favorit": "No Longer Human",
    "Idola": "Nabi Muhammad SAW",
    "Motto": "Tetaplah di jalan tuhan, walaupun kadang belok dikit"
}

for label, value in data.items():
    row = tk.Frame(card, bg="white")
    row.pack(anchor="w", pady=3)
    tk.Label(row, text=f"{label} :", font=("Segoe UI", 10, "bold"),
             fg="#555", bg="white").pack(side="left")
    tk.Label(row, text=value, font=("Segoe UI", 10),
             bg="white").pack(side="left")

Button(
    app,
    text="Tutup",
    bootstyle="danger rounded",  
    command=app.quit,
    width=15
).pack(pady=5)

app.mainloop()
