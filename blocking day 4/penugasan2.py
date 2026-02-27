import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

TARIF_PER_JAM = 2000

def hitung_biaya():
    try:
        masuk = datetime.strptime(entry_masuk.get(), "%H:%M")
        keluar = datetime.strptime(entry_keluar.get(), "%H:%M")

        selisih = keluar - masuk
        jam = selisih.seconds / 3600
        total = int(jam * TARIF_PER_JAM)

        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, total)

        tree.insert("", "end", values=(
            entry_nopol.get(),
            entry_masuk.get(),
            entry_keluar.get(),
            total
        ))

    except:
        messagebox.showerror("Error", "Gunakan format waktu HH:MM")

# Window utama
root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("700x500")

# Frame Input
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="No Plat Polisi").grid(row=0, column=0, sticky="w")
entry_nopol = tk.Entry(frame)
entry_nopol.grid(row=0, column=1)

tk.Label(frame, text="Waktu Masuk (HH:MM)").grid(row=1, column=0, sticky="w")
entry_masuk = tk.Entry(frame)
entry_masuk.grid(row=1, column=1)

tk.Label(frame, text="Waktu Keluar (HH:MM)").grid(row=2, column=0, sticky="w")
entry_keluar = tk.Entry(frame)
entry_keluar.grid(row=2, column=1)

tk.Label(frame, text="Biaya").grid(row=3, column=0, sticky="w")
entry_biaya = tk.Entry(frame)
entry_biaya.grid(row=3, column=1)

tk.Button(frame, text="Hitung", command=hitung_biaya).grid(row=4, column=1, pady=10)

# Label Tarif Besar
tk.Label(root, text="Biaya Per Jam", font=("Arial", 18)).pack()
tk.Label(root, text="Rp. 2.000", font=("Arial", 28), fg="red").pack()

# Tabel Data
columns = ("NoPol", "Masuk", "Keluar", "Biaya")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(pady=10)

root.mainloop()