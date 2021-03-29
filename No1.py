class Bunga:
    bahasa_inggris ="Flower"

    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
            
    @classmethod
    def segar(cls) :
        print(f"{cls.bahasa_inggris} segar")
        
    @staticmethod
    def layu():
        print(f"{Bunga.bahasa_inggris} layu")

    def bau(self):
        print(f"{self.nama} harum")

class Mawar(Bunga):
    pass

class Melati(Bunga):
    pass
        

class Mawar(Bunga):
    nama_latin = "Rosa spp"

    def bau(self):
        print(f"{self.nama} memiliki aroma")


class Melati(Bunga):
    nama_latin = "Jasminum sambac"

    def bau(self):
        print(f"{self.nama} memiliki aroma")

Mawar = Bunga('Mawar', 'Merah')
Melati = Bunga('Melati', 'Putih')

Mawar.bau()
Melati.bau()

Mawar.segar()
Melati.segar()





