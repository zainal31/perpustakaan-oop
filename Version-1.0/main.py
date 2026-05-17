from perpustakaan import Perpustakaan
from buku import Buku

perpus = Perpustakaan("Pusat")

katalog_perpustakaan = {
    "B01": {"item": Buku("B01", "Filosofi Teras", "Henry Manampiring"), "tersedia": True},
    "B02": {"item": Buku("B02", "Laskar Pelangi", "Andrea Hirata"), "tersedia": True},
    "B03": {"item": Buku("B03", "Atomic Habits", "James Clear"), "tersedia": True},
    "B04": {"item": Buku("B04", "Bumi Manusia", "Pramoedya Ananta Toer"), "tersedia": True},
    "B05": {"item": Buku("B05", "Hujan", "Tere Liye"), "tersedia": True},
    "B06": {"item": Buku("B06", "5 CM", "Donny Dhirgantoro"), "tersedia": True},
    "B07": {"item": Buku("B07", "Laut Bercerita", "Leila S. Chudori"), "tersedia": True},
    "B08": {"item": Buku("B08", "Perahu Kertas", "Dee Lestari"), "tersedia": True},
    "B09": {"item": Buku("B09", "3726 MDPL", "Nurwina Sari"), "tersedia": True},
}

while True:
    print(f" MENU PERPUSTAKAAN ".center(50, "="))
    print("1. Tampilkan Katalog Buku")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Keluar")

    pilihan = input("Pilihan Menu (1-4): ")

    if pilihan == "1":
        perpus.show_catalog(katalog_perpustakaan)
    elif pilihan == "2":
        item_id = input("Masukkan ID Buku yang ingin dipinjam (Contoh: B01): ")
        perpus.peminjaman(katalog_perpustakaan, item_id)
    elif pilihan == "3":
        item_id = input("Masukkan ID Buku yang ingin dikembalikan: ")
        tgl_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")
        tgl_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")
        perpus.pengembalian(katalog_perpustakaan, item_id, tgl_pinjam, tgl_kembali)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan perpustakaan.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")