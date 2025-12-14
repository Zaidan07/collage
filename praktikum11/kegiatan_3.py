import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style

def hitung():
    try:
        lbl_hasil.config(text=f"Luas = {int(entry.get())**2}")
    except ValueError:
        messagebox.showerror("Error", "Input harus berupa angka!")
        entry.delete(0, tk.END)

root = tk.Tk()
root.geometry("300x250")
root.title("Luas Persegi")
Style(theme="darkly")

tk.Label(root, text="Persegi", font=("Arial", 14, "bold")).pack(pady=15)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Sisi :").pack(side="left")
entry = tk.Entry(frame)
entry.pack(side="left")

lbl_hasil = tk.Label(root, text="Luas = 0", font=("Arial", 12, "bold"))

tk.Button(root, text="Hitung Luas", command=hitung).pack(pady=10)

lbl_hasil.pack()
root.mainloop()