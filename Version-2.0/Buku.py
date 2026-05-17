from ItemPerpustakaan import ItemPerpustakaan

class Buku(ItemPerpustakaan):
    def __init__(self, id_item, judul, penulis):
        super().__init__(id_item, judul)
        self.penulis = penulis

    def deskripsi(self):
        return f"[{self.get_id()}] Buku: {self.get_judul()}     | Penulis: {self.penulis}"