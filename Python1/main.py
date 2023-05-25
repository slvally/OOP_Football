from tim import tim #import kelas tim

# deklarasi variabel lokal
n=2
i=0

# membuat array kosong
mtim = [None] * 2
# deklarasi tim pertama pada mtim
mtim[0] = tim()
# isi tim pertama
mtim[0].setnamatim("Waifu1")
mtim[0].setasal("Anime1")
mtim[0].settahun(2002)
mtim[0].setpemain("Ruminas, Destiny, Sasha, Lynn, Siesta")
# isi tim kedua
mtim[1] = tim("Waifu2", "Anime2", 2002, "Hu Tao, Ganyu, Yae, Miko, Ueno, Marin")

# tampilkan tim
for x in range(n):
    print("Nama Tim-" + str(x+1) + " : " + str(mtim[x].getnamatim()))
    print("Asal : " + str(mtim[x].getasal()))
    print("tahun : " + str(mtim[x].gettahun()))
    print("Pemain : " + str(mtim[x].getpemain()) + "\n")
