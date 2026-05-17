from ManajerPerpustakaan import ManajerPerpustakaan

# Kode warna ANSI
RESET  = "\033[0m"
KUNING = "\033[93m"
CYAN   = "\033[96m"
TEBAL  = "\033[1m"


def main():
    perpus = ManajerPerpustakaan()
    while True:
        print(f"\n{TEBAL}{CYAN}{'='*50}{RESET}")
        print(f"{TEBAL}{CYAN}{'Perpustakaan Nasional'.center(50)}{RESET}")
        print(f"{TEBAL}{CYAN}{'='*50}{RESET}")
        print(f"{KUNING}1. Tambah Buku Baru{RESET}")
        print(f"{KUNING}2. Tampilkan Semua Koleksi{RESET}")
        print(f"{KUNING}3. Urutkan Koleksi (Bubble Sort){RESET}")
        print(f"{KUNING}4. Cari Buku (Binary Search){RESET}")
        print(f"{KUNING}5. Keluar{RESET}")

        pilihan = int(input("\nPilih menu (1-5): "))

        if pilihan == 1:
            perpus.tambah_buku_baru()
        elif pilihan == 2:
            perpus.tampilkan_koleksi()
        elif pilihan == 3:
            perpus.urutkan_koleksi()
        elif pilihan == 4:
            id_target = int(input("Masukkan ID Buku yang dicari: "))
            perpus.cari_buku(id_target)
        elif pilihan == 5:
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
main()

