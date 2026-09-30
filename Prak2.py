pi = 3.14

luas = lambda r: pi * r ** 2

print("\n======== HITUNG LUAS LINGKARAN ========")
r = float(input("Masukkan jari-jari lingkaran: "))
print("Luas lingkaran dengan jari-jari " + str(r) + " adalah " + str(round(luas(r), 2)))