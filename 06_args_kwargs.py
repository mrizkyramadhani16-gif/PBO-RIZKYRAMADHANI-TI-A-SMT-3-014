def jumlahkan(*angka): return sum(angka)
def data(**kwargs):
    for k,v in kwargs.items(): print(k,":",v)
print(jumlahkan(10,20,30))
data(nama="Rizky",nim="2595114014")
