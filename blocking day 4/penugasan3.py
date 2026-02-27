import tkinter as tk
from tkinter import messagebox

def simpan_data():
    nama = entry_nama.get()
    if nama == "":
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
    else:
        messagebox.showinfo("Sukses", "Data berhasil disimpan!")

def hapus_data():
    entry_nama.delete(0, tk.END)
    entry_tgl.delete(0, tk.END)
    entry_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_ayah.delete(0, tk.END)
    entry_ibu.delete(0, tk.END)
    entry_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

root = tk.Tk()
root.title("DATA SISWA BARU")
root.geometry("550x600")
root.configure(bg="#dcdcdc")

judul = tk.Label(root, text="DATA SISWA BARU",
                 font=("Arial", 18, "bold"),
                 bg="#a8dadc",
                 pady=10)
judul.pack(fill="x")

frame = tk.Frame(root, bg="#dcdcdc", padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Nama Lengkap", bg="#dcdcdc").grid(row=0, column=0, sticky="w")
entry_nama = tk.Entry(frame, width=40)
entry_nama.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Tanggal Lahir", bg="#dcdcdc").grid(row=1, column=0, sticky="w")
entry_tgl = tk.Entry(frame, width=40)
entry_tgl.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Asal Sekolah", bg="#dcdcdc").grid(row=2, column=0, sticky="w")
entry_sekolah = tk.Entry(frame, width=40)
entry_sekolah.grid(row=2, column=1, pady=5)

tk.Label(frame, text="NISN", bg="#dcdcdc").grid(row=3, column=0, sticky="w")
entry_nisn = tk.Entry(frame, width=40)
entry_nisn.grid(row=3, column=1, pady=5)

tk.Label(frame, text="Nama Ayah", bg="#dcdcdc").grid(row=4, column=0, sticky="w")
entry_ayah = tk.Entry(frame, width=40)
entry_ayah.grid(row=4, column=1, pady=5)

tk.Label(frame, text="Nama Ibu", bg="#dcdcdc").grid(row=5, column=0, sticky="w")
entry_ibu = tk.Entry(frame, width=40)
entry_ibu.grid(row=5, column=1, pady=5)

tk.Label(frame, text="Nomor Telepon / HP", bg="#dcdcdc").grid(row=6, column=0, sticky="w")
entry_hp = tk.Entry(frame, width=40)
entry_hp.grid(row=6, column=1, pady=5)

tk.Label(frame, text="Alamat", bg="#dcdcdc").grid(row=7, column=0, sticky="nw")
text_alamat = tk.Text(frame, width=30, height=5)
text_alamat.grid(row=7, column=1, pady=5)

frame_btn = tk.Frame(root, bg="#a8dadc", pady=10)
frame_btn.pack(fill="x")

btn_simpan = tk.Button(frame_btn, text="Simpan", width=10,
                       bg="#e76f51", fg="white",
                       command=simpan_data)
btn_simpan.pack(side="right", padx=10)

btn_hapus = tk.Button(frame_btn, text="Hapus", width=10,
                      bg="#e76f51", fg="white",
                      command=hapus_data)
btn_hapus.pack(side="right")

root.mainloop()