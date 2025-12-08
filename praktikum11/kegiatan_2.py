import tkinter as tk

app = tk.Tk()
app.title("Kalkulator")
app.geometry("330x250")

tk.Label(app, text="Angka 1").pack(anchor="w", padx=20, pady=(15,0))
e1 = tk.Entry(app, width=20)
e1.pack(padx=20)

tk.Label(app, text="Angka 2").pack(anchor="w", padx=20, pady=(10,0))
e2 = tk.Entry(app, width=20)
e2.pack(padx=20)

def op(fn):
    try:
        a, b = float(e1.get()), float(e2.get())
        result["text"] = fn(a, b)
    except:
        result["text"] = "Input salah"

btns = tk.Frame(app)
btns.pack(pady=18)

ops = {
    "+": lambda a,b: a+b,
    "-": lambda a,b: a-b,
    "x": lambda a,b: a*b,
    "/": lambda a,b: a/b if b else "Tidak bisa"
}

for i, (t, f) in enumerate(ops.items()):
    tk.Button(btns, text=t, width=5, command=lambda fn=f: op(fn)).grid(row=0, column=i, padx=5)

tk.Label(app, text="Hasil").pack()
result = tk.Label(app, text="", font=("Arial", 12))
result.pack()

app.mainloop()
