from buku import Buku
from datetime import datetime

class Perpustakaan(Buku):
    def __init__(self, nama_cabang):
        super().__init__(None, None, None)  
        self.nama_cabang = nama_cabang

    def show_catalog(self, katalog):
        print("=" * 72)
        print(f"  {'ID':<6} | {'JUDUL BUKU':<25} | {'PENULIS':<22} | STATUS")
        print("-" * 72)
        for id_buku, data in katalog.items(): # digunakan untuk mengakses setiap item dalam katalog
            buku = data["item"]     
            status = "Tersedia" if data["tersedia"] else "Dipinjam"
            print(f"  {id_buku:<6} | {buku.get_judul():<25} | {buku.get_penulis():<22} | {status}") 
        print("=" * 72) 
    
    def peminjaman(self, katalog, item_id): 
        if item_id not in katalog:
            print(f"[GAGAL] Buku dengan ID '{item_id}' tidak ditemukan.")
            return False

        if not katalog[item_id]["tersedia"]:    
            print(f"[GAGAL] Buku '{katalog[item_id]['item'].get_judul()}' sedang dipinjam.")
            return False

        katalog[item_id]["tersedia"] = False
        print(f"[SUKSES] Berhasil meminjam: {katalog[item_id]['item'].get_judul()}")
        return True

    def pengembalian(self, katalog, item_id, tgl_pinjam, tgl_kembali):
        if item_id not in katalog:
            print(f"[GAGAL] Buku dengan ID '{item_id}' tidak ditemukan.")
            return False

        if katalog[item_id]["tersedia"]:
            print(f"[GAGAL] Buku '{katalog[item_id]['item'].get_judul()}' sudah tersedia di perpustakaan.")
            return False

        try:        # digunakan untuk mengubah string tanggal menjadi objek datetime
            d1 = datetime.strptime(tgl_pinjam, "%Y-%m-%d")
            d2 = datetime.strptime(tgl_kembali, "%Y-%m-%d")
        except ValueError:  # digunakan untuk menangani error jika format tanggal tidak valid   
            print(f"[GAGAL] Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
            return False
        
        batas_hari = 7   
        selisih_hari = (d2 - d1).days   
        hari_terlambat = max(0, selisih_hari - batas_hari)   

        buku = katalog[item_id]["item"] # digunakan untuk mengakses setiap item dalam katalog
        denda = buku.hitung_denda(hari_terlambat) 

        katalog[item_id]["tersedia"] = True

        print(f"[SUKSES] Pengembalian: {buku.get_judul()}")
        print(f"Total Durasi: {selisih_hari} hari (Batas: {batas_hari} hari)")

        if hari_terlambat > 0:
            print(f"Terlambat: {hari_terlambat} hari. Total Denda: Rp {denda:,}")
        else:
            print("Tidak ada denda. Terima kasih telah mengembalikan tepat waktu.")
        return True

