class Buku:
    def __init__(self, item_id, judul, penulis):
        self.__item_id = item_id
        self.__judul = judul
        self.__penulis = penulis
        self.__status = True

    # getter digunakan untuk mengakses nilai atribut private
    def get_item_id(self):
        return self.__item_id

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_status(self):
        return self.__status

    # setter digunakan untuk mengubah nilai atribut private
    def set_item_id(self, item_id):
        self.__item_id = item_id

    def set_judul(self, judul):
        self.__judul = judul

    def set_penulis(self, penulis):
        self.__penulis = penulis

    def set_status(self, status):
        self.__status = status

    def hitung_denda(self, hari_terlambat):
        return hari_terlambat * 2000