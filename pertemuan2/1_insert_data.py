# contoh input data ke file
print('Pencatatan Laptop Darusinau.com :: Tulis File')

print('Input merk laptop')
merk = input('> ')

print('Input kapasitas RAM laptop (dalam GB)')
ram = input('> ')

print(f"anda telah meng-input laptop `{merk}` dengan RAM `{ram}` GB")

file = open('daftar_laptop.txt', 'a') # gunakan atribut a untuk append (menambahkan isi)
file.writelines(f"{merk},{ram}\n")
file.close()
print('simpan data selesai')
