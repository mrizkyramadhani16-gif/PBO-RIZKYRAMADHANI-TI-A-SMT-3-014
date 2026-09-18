# finally
try:
    print('Proses dimulai.')
    hasil = 10 / 2
    print('Hasil:', hasil)
except ZeroDivisionError:
    print('Terjadi kesalahan pembagian.')
finally:
    print('Blok finally selalu dijalankan.')
