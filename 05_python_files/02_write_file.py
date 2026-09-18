# Menulis ke file
with open('catatan.txt', 'w') as file:
    file.write('Halo, ini file Python.\n')
    file.write('Belajar File Handling bersama Python.')
print('Data berhasil ditulis.')
