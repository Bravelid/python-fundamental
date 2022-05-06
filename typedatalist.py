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

print("\nperintah del")
daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal', "4DX"]
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nperintah del dengan list comprehension")
daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal', "4DX"]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nperintah del dengan list comprehension  start")
daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal', "4DX"]
del daftar_buku[1:-1]#START END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nperintah del dengan list comprehension  start step")
daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal', "4DX"]
del daftar_buku[0::2]#START END STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nmembuat list baru")
daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal', "4DX"]
bukubaru = daftar_buku[:]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print("\nlist baru")
for i in range(0, len(bukubaru)):
    print(bukubaru[i])

print("\nmembuat list baru dengan list comprehesion:ganjil")
daftar_buku = ['1. Seven Habits', '2. Seven Deadly', '3. Return of Royal', "4. 4DX"]
bukubaru = daftar_buku[0::2]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print("\nlist baru")
for i in range(0, len(bukubaru)):
    print(bukubaru[i])

print("\nmembuat list baru dengan list comprehesion:genap")
daftar_buku = ['1. Seven Habits', '2. Seven Deadly', '3. Return of Royal', "4. 4DX"]
bukubaru = daftar_buku[1::2]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print("\nlist baru")
for i in range(0, len(bukubaru)):
    print(bukubaru[i])

print("\nmembuat list baru dengan list comprehesion:ambil tengah dan belakang")
daftar_buku = ['1. Seven Habits', '2. Seven Deadly', '3. Return of Royal', "4. 4DX"]
bukubaru = daftar_buku[0:-1:2]
print("\nlist baru")
for i in range(0, len(bukubaru)):
    print(bukubaru[i])

print("\nmembuat list baru dengan list comprehesion simple print")
daftar_buku = ['1. Seven Habits', '2. Seven Deadly', '3. Return of Royal', "4. 4DX"]
bukubaru = daftar_buku[0::3]
print(daftar_buku[0:2])
