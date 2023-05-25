from tkinter import N
from tim import tim #import kelas tim

# masukkan banyak tim
n = int(input('masukkan banyak tim : '))
# masukkan banyak pemain
m = int(input('masukkan banyak pemain : '))

print("")

# membuat array kosong
mtim = [None] * n

# Deklarasi dan mengisi variabel sementara
namatim = ""
asal = ""
tahun = 0
pemain = [None] * m
for x in range(n):
    mtim[x] = tim()
    namatim = input('input nama tim ke-' + str(x+1) + ' : ')
    asal = input('input asal tim : ')
    tahun = int(input('input tahun tim : '))
    print('input ' + str(m) + ' pemain : ')
    for z in range(m):
        pemain[z] = input()
    mtim[x] = tim(namatim, asal, tahun, pemain)
    pemain = [None] * m

# tampilkan tim
print('\n\nDaftar Tim\n==========')
for x in range(n):
    print("Nama Tim-" + str(x+1) + " : " + str(mtim[x].getnamatim()))
    print("Asal : " + str(mtim[x].getasal()))
    print("tahun : " + str(mtim[x].gettahun()))
    print('Pemain : ')
    for z in range(m):
        print('- ' + str(mtim[x].getpemain(z)))
    if x != n-1:
        print("")