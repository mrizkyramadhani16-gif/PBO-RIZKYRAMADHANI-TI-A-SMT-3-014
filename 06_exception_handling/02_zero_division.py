# Menangani pembagian dengan nol
try:
    a = int(input('Angka pertama: '))
    b = int(input('Angka kedua: '))
    print('Hasil:', a / b)
except ZeroDivisionError:
    print('Tidak boleh membagi dengan nol.')
except ValueError:
    print('Input harus berupa angka.')
