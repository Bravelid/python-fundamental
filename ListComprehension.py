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
del daftar_buku[1:-1]  # START END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nperintah del dengan list comprehension  start step")
daftar_buku = ['Seven Habits', 'Seven Deadly', 'Return of Royal', "4DX"]
del daftar_buku[0::2]  # START END STEP
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