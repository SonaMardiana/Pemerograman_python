def tambah_barang(inventaris, nama, harga, stok):
    if not nama.strip():
        raise ValueError("Nama barang tidak boleh kosong.")
    if nama in inventaris:
        raise ValueError("Barang sudah ada di inventaris.")
    if harga < 0 or stok < 0:
        raise ValueError("Harga dan stok tidak boleh negatif.")
    inventaris[nama] = (harga, stok)


def update_stok(inventaris, nama, stok_baru):
    if nama not in inventaris:
        raise ValueError("Barang tidak ditemukan.")
    if stok_baru < 0:
        raise ValueError("Stok tidak boleh negatif.")
    harga, _ = inventaris[nama]
    inventaris[nama] = (harga, stok_baru)


def cari_barang_berdasarkan_harga(inventaris, harga_minimum, harga_maksimum):
    if harga_minimum > harga_maksimum:
        raise ValueError("Harga minimum tidak boleh melebihi harga maksimum.")
    return {
        nama: data
        for nama, data in inventaris.items()
        if harga_minimum <= data[0] <= harga_maksimum
    }


def hitung_total_nilai(inventaris):
    return sum(harga * stok for harga, stok in inventaris.values())


def tampilkan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris masih kosong.")
        return
    for nama, (harga, stok) in inventaris.items():
        print(f"- {nama}: harga Rp{harga:g}, stok {stok}")


def main():
    inventaris = {
        "Buku": (15000, 10),
        "Pensil": (3000, 25),
        "Penghapus": (2000, 15),
    }

    while True:
        print("\n=== Inventaris Toko ===")
        print("1. Tampilkan inventaris")
        print("2. Tambah barang")
        print("3. Update stok")
        print("4. Cari barang berdasarkan rentang harga")
        print("5. Hitung total nilai inventaris")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                tampilkan_inventaris(inventaris)
            elif pilihan == "2":
                nama = input("Nama barang: ").strip()
                harga = float(input("Harga: "))
                stok = int(input("Stok: "))
                tambah_barang(inventaris, nama, harga, stok)
                print("Barang berhasil ditambahkan.")
            elif pilihan == "3":
                nama = input("Nama barang: ").strip()
                stok = int(input("Stok baru: "))
                update_stok(inventaris, nama, stok)
                print("Stok berhasil diperbarui.")
            elif pilihan == "4":
                minimum = float(input("Harga minimum: "))
                maksimum = float(input("Harga maksimum: "))
                hasil = cari_barang_berdasarkan_harga(inventaris, minimum, maksimum)
                if hasil:
                    tampilkan_inventaris(hasil)
                else:
                    print("Tidak ada barang dalam rentang harga tersebut.")
            elif pilihan == "5":
                print(f"Total nilai inventaris: Rp{hitung_total_nilai(inventaris):g}")
            elif pilihan == "0":
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak tersedia.")
        except ValueError as error:
            print(f"Input tidak valid: {error}")


if __name__ == "__main__":
    main()
