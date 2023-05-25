# deklarasi kelas tim
class tim():

    # deklarasi variabel lokal
    __namatim = ""
    __asal = ""
    __tahun = 0
    __pemain = [None] * 20
    i = 0

    # konstruktor
    def __init__(self, namatim="", asal="", tahun=0, pemain=[None] * 20):
        self.__namatim = namatim
        self.__asal = asal
        self.__tahun = tahun
        self.__pemain = pemain

    # get dan set setiap variabel
    def setnamatim(self, namatim):
        self.__namatim = namatim
    def getnamatim(self):
        return self.__namatim
    def setasal(self, asal):
        self.__asal = asal
    def getasal(self):
        return self.__asal
    def settahun(self, tahun):
        self.__tahun = tahun
    def gettahun(self):
        return self.__tahun
    def setpemain(self, pemain):
        self.__pemain[len(self.__pemain)] = pemain
    def getpemain(self, i=0):
        return self.__pemain[i]
        