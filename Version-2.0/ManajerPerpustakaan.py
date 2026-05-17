from Buku import Buku 
from Penulis import Penulis

# Kode warna ANSI
RESET  = "\033[0m"
HIJAU  = "\033[92m"
MERAH  = "\033[91m"
KUNING = "\033[93m"
CYAN   = "\033[96m"
TEBAL  = "\033[1m"

class ManajerPerpustakaan:
    def __init__(self):
        self.koleksi = [] 
        self.terurut = False

    def validasi_id_unik(self, id_baru):
        for buku in self.koleksi:
            if buku.get_id() == id_baru:
                return False
        return True

    def tambah_buku_baru(self):
        print(f"\n{CYAN}--- Form Penambahan Buku Baru ---{RESET}")
        try:
            id_item = int(input("Masukkan ID Buku (Angka): "))
        except ValueError:
            print(f"{MERAH}[ERROR] ID harus angka{RESET}")
            return

        if not self.validasi_id_unik(id_item):
            print(f"{MERAH}[ERROR] ID sudah digunakan{RESET}")
            return

        judul = input("Masukkan Judul Buku: ")
        nama = input("Masukkan Nama Penulis: ")
        kewarganegaraan = input("Masukkan Asal Negara Penulis: ")
        
        penulis = Penulis(nama, kewarganegaraan)
        buku = Buku(id_item, judul, penulis)
        self.koleksi.append(buku)
        self.terurut = False
        print(f"{HIJAU}[SUKSES] '{buku.get_judul()}' karya {penulis.nama} berhasil ditambahkan.{RESET}")

    def tampilkan_koleksi(self):
        if not self.koleksi:
            print(f"{KUNING}Koleksi masih kosong.{RESET}")
            return
        
        print(f"\n{TEBAL}ID | Informasi Buku{RESET}")
        print("-"*50)
        for buku in self.koleksi:
            print(buku.deskripsi())

    def urutkan_koleksi(self):
        n = len(self.koleksi)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.koleksi[j].get_id() > self.koleksi[j+1].get_id():
                    self.koleksi[j], self.koleksi[j+1] = self.koleksi[j+1], self.koleksi[j]
        self.terurut = True
        print(f"{HIJAU}[SISTEM] Koleksi berhasil diurutkan{RESET}")

    def cari_buku(self, id_target):
        if not self.terurut:
            print(f"{KUNING}[Peringatan] Mohon untuk mengurutkan terlebih dahulu!{RESET}")
            print(f"{MERAH}[HASIL] ID {id_target} tidak ditemukan.{RESET}")
            return None

        left = 0
        right = len(self.koleksi) - 1
        buku_ditemukan = None

        while left <= right:
            mid = (left + right) // 2
            mid_id = self.koleksi[mid].get_id()
            
            if mid_id == id_target:
                buku_ditemukan = self.koleksi[mid]
                break
            elif id_target < mid_id:
                right = mid - 1
            else:
                left = mid + 1

        if buku_ditemukan:
            print(f"{HIJAU}[DITEMUKAN] Buku: {buku_ditemukan.get_judul()}  | Penulis: {buku_ditemukan.penulis.nama}{RESET}")
            print(f"Detail Penulis: {buku_ditemukan.penulis}") 
            return buku_ditemukan
        else:
            print(f"{MERAH}[HASIL] ID {id_target} tidak ditemukan.{RESET}")
            return None