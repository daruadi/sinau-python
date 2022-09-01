# update dan delete data pada dasarnya sama
# update di memory kemudian rewrite semua isi file

print('Pencatatan Laptop Darusinau :: Update File')
file = open('daftar_laptop.txt')
lines = file.readlines()

print("Input merk laptop yg ingin di-update")
merk = input("> ")

flag_data_ditemukan = False

for index, value in enumerate(lines):
    if merk in value: # cari merk dalam baris case-sensitive
        print(f"Laptop merk {merk} ditemukan")
        print("Input kapasitas ram baru")
        ram = input('> ')
        lines[index] = f"{merk},{ram}\n" # create data baru di lines ke index
        data_split = lines[index].split(',')
        print(f"Laptop merk {data_split[0]}, diperbarui dgn ram {data_split[1].strip()}")
        flag_data_ditemukan = True
file.close() # tutup file di proses sebelumnya
print("pencarian selesai")

if flag_data_ditemukan:
    # buka file baru lagi untuk write data dari memory
    file = open('daftar_laptop.txt', 'w')
    file.writelines(lines)
    file.close()
    print('simpan data selesai')
else:
    print(f"laptop merk {merk} tidak ditemukan")
