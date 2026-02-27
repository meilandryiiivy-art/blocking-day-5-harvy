# =========================================
# 1. Keliling dan Luas
# =========================================

# PERSEGI
sisi = float(input("Masukkan sisi persegi: "))
luas_persegi = sisi * sisi
keliling_persegi = 4 * sisi
print("Luas Persegi:", luas_persegi)
print("Keliling Persegi:", keliling_persegi)

# PERSEGI PANJANG
panjang = float(input("\nMasukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
luas_pp = panjang * lebar
keliling_pp = 2 * (panjang + lebar)
print("Luas Persegi Panjang:", luas_pp)
print("Keliling Persegi Panjang:", keliling_pp)

# TRAPESIUM
a = float(input("\nMasukkan sisi atas trapesium: "))
b = float(input("Masukkan sisi bawah trapesium: "))
t = float(input("Masukkan tinggi trapesium: "))
c = float(input("Masukkan sisi miring kiri: "))
d = float(input("Masukkan sisi miring kanan: "))

luas_trapesium = 0.5 * (a + b) * t
keliling_trapesium = a + b + c + d
print("Luas Trapesium:", luas_trapesium)
print("Keliling Trapesium:", keliling_trapesium)