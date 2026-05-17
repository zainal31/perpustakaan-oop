class Penulis:
    def __init__(self, nama, kewarganegaraan):
        self.nama = nama
        self.kewarganegaraan = kewarganegaraan

    def __str__(self):
        return f"{self.nama} ({self.kewarganegaraan})"