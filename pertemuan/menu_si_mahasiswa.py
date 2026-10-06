from status_mahasiswa import input_mahasiswa, tampilkan_laporan
from diskon_biaya import input_data_diskon, tampilkan_hasil_diskon
from peringatan_stok import data_inventaris, tampilkan_laporan_stok
from validasi_data import validasi_mahasiswa_data


def submenu_status_mahasiswa():
    """Menu untuk cek status mahasiswa."""
    print("\n=== CEK STATUS MAHASISWA ===")
    data = input_mahasiswa()
    tampilkan_laporan(data)


def submenu_diskon_biaya():
    """Menu untuk menghitung diskon biaya."""
    print("\n=== HITUNG DISKON BIAYA ===")
    data = input_data_diskon()
    tampilkan_hasil_diskon(data)


def submenu_peringatan_stok():
    """Menu untuk cek peringatan stok."""
    print("\n=== CEK PERINGATAN STOK ===")
    inventaris = data_inventaris()
    tampilkan_laporan_stok(inventaris)


def submenu_validasi_data():
    """Menu untuk validasi data mahasiswa."""
    print("\n=== VALIDASI DATA MAHASISWA ===")
    nim = input("NIM (10 digit): ").strip()

    try:
        ipk = float(input("IPK: ").replace(",", "."))
    except ValueError:
        ipk = -1.0

    try:
        sks = int(input("SKS: "))
    except ValueError:
        sks = -1

    try:
        semester = int(input("Semester: "))
    except ValueError:
        semester = -1

    errors = validasi_mahasiswa_data(nim, ipk, sks, semester)

    if errors:
        print("\nData tidak valid:")
        for msg in errors:
            print(f"- {msg}")
    else:
        print("\nData mahasiswa valid.")


def tampilkan_menu():
    """Menampilkan menu utama."""
    print("\n=== MENU SISTEM INFORMASI MAHASISWA ===")
    print("1. Cek Status Mahasiswa")
    print("2. Hitung Diskon Biaya")
    print("3. Cek Peringatan Stok")
    print("4. Validasi Data Mahasiswa")
    print("0. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (0-4): ").strip()

        if pilihan == "1":
            submenu_status_mahasiswa()
        elif pilihan == "2":
            submenu_diskon_biaya()
        elif pilihan == "3":
            submenu_peringatan_stok()
        elif pilihan == "4":
            submenu_validasi_data()
        elif pilihan == "0":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka 0-4.")


if __name__ == "__main__":
    main()
