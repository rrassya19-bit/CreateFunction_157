def konversi(suhu, satuan):
    "Konversi suhu Celsius ke Fahrenheit dan sebaliknya"
    if satuan == "C":
        hasil = (suhu * 9 / 5) + 32
    elif satuan == "F":
        hasil = (suhu - 32) * 5 / 9
    else:
        hasil = None
    return hasil

print("======== KONVERSI SUHU ========")
suhu = float(input("Masukkan nilai suhu: "))
satuan = input("Masukkan satuan suhu ('C' untuk Celsius atau 'F' untuk Fahrenheit): ")

hasil = konversi(suhu, satuan)

if satuan == "C":
    print(str(suhu) + "°C = " + str(round(hasil, 2)) + "°F")
elif satuan == "F":
    print(str(suhu) + "°F = " + str(round(hasil, 2)) + "°C")
else:
    print("Satuan suhu tidak dikenal!")