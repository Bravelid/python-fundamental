# Sequential

print("Ibu memberi perintah,'nak belikan ibu 1 botol susu ,kalau ada telur maka belilah 6 butir telur'")
print("Anak menjawab,'Oke bu'")
print("Anak pergi ke toko")
print("Apakah ada susu mas?")

# Percabangan
totalsusu = 100
jumlahtelur = 3000
print(f"Jumlah susu adalah {totalsusu} botol")
print(f"Jumlah telur adalah {jumlahtelur}")

if totalsusu > 0:
    print("Anak mengecek uang dan cukup")
    print("Anak jadi membeli 1 botol susu")
    if jumlahtelur > 0:
        print("anak membeli 6 butir telur")
        print("yang anak beli adalah 1 botol susu dan 6 butir telur")
else:
    print("Anak tidak jadi membeli susu dan telur ")

print("Anak pulang dari toko")
print("Anak menyerahkan hasil belanjanya")
