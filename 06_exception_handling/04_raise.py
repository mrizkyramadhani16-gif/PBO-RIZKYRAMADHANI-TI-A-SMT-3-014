# raise
try:
    nilai = int(input('Masukkan nilai: '))
    if nilai < 0 or nilai > 100:
        raise ValueError('Nilai harus berada di antara 0 dan 100.')
    print('Nilai valid:', nilai)
except ValueError as error:
    print('Error:', error)
