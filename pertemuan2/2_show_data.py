# contoh baca data dari file
print('Pencatatan Laptop Darusinau.com :: Baca File')
file = open('daftar_laptop.txt')
lines = file.readlines()
file.close() #langsung tutup file karena dibawah sudah tidak akses file lagi

# cetak data by index
print(f"data pertama belum diolah {lines[0]}")

# cetak data by index dan diolah
data_kedua = lines[1].split(",")
print(f"data kedua sudah diolah: merk {data_kedua[0]}, kapasitas ram {data_kedua[1]}")

# cetak data dengan loop
print('cetak dengan loop')
for line in lines:
    data_split = line.split(",")
    print(f"Laptop merk {data_split[0]}, memiliki ram {data_split[1].strip()}")
