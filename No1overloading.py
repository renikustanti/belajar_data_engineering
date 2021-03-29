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

class Mawar:
    nama_latin = "Rosa spp"

    def bau(self, bau=None):
        if bau == None:
            print("Tidak berbau")
        else:
            print(f"{self.nama} memiliki bau{bau}")
        
class Melati(Bunga):
    nama_latin = "Jasminum sambac"

    def tampak(self):
        print(f"{self.nama} kelihatan layu")

Mawar = Bunga('Mawar', 'Merah')
Melati = Bunga('Melati', 'Putih')

Mawar.bau()
Melati.bau()


