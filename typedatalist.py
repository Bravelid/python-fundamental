daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal']
print('tampilkan semua daftar buku yang berada dalam list')
print(daftar_buku)

print('\nMenampilkan daftar buku dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nMenampilkan daftar buku yang ingin ditampilkan dengan list')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nMenampilkan daftar buku dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMenampilkan daftar buku dengan tipe data berbeda")
daftar_buku = [21313, "World of war", 43.3, "AANG"]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMenambahkan buku dengan append')
daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal', "4DX"]
daftar_buku.append(1212)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMenghapus semua data list")
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("mengganti elemen pertama data list")
daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal', "4DX"]
daftar_buku[0] = 'Siuuuu'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMengambil elemen kedua pada data list")
buku = daftar_buku.pop(3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nmenampilkan yang sudah diambil")
print(buku)

print("\n penggunaan Pop")
daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal', "4DX"]
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\n penggunaan Pop - ")
daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal', "4DX"]
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
