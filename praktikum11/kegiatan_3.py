import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("Luas Persegi")

tk.Label(root, text="Bangun Geometri: Persegi", font=("Arial", 14, "bold")).pack(pady=15)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Sisi :").pack(side=tk.LEFT)
entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

lbl_hasil = tk.Label(root, text="Luas = 0", font=("Arial", 12, "bold"))

tk.Button(root, text="Hitung Luas", command=lambda: lbl_hasil.config(text=f"Luas = {int(entry.get())**2}")).pack(pady=10)

lbl_hasil.pack()
root.mainloop()