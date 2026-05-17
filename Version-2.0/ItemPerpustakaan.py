from abc import ABC, abstractmethod

class ItemPerpustakaan(ABC):
    def __init__(self, id_item, judul):
        self.id_item = id_item
        self.__judul = judul

    @abstractmethod
    def deskripsi(self):
        pass

    def get_id(self):
        return self.id_item

    def get_judul(self):
        return self.__judul