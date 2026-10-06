def cek_status_mahasiswa(ipk: float, sks: int) -> str:
    """Menentukan status mahasiswa berdasarkan IPK dan SKS."""
    if ipk >= 2.0 and sks >= 18:
        return "Aktif"
    if 1.5 <= ipk < 2.0:
        return "Peringatan"
    return "Tidak Aktif"


def input_mahasiswa() -> list[dict]:
    """Menerima data 5 mahasiswa dari input pengguna."""
    data = []
    for i in range(1, 6):
        print(f"\nMahasiswa {i}")

        while True:
            nim = input("NIM: ").strip()
            if nim:
                break
            print("NIM tidak boleh kosong.")

        nama = input("Nama: ").strip()

        while True:
            try:
                ipk = float(input("IPK: ").replace(",", "."))
                if 0.0 <= ipk <= 4.0:
                    break
                print("IPK harus antara 0.0 sampai 4.0.")
            except ValueError:
                print("IPK harus berupa angka.")

        while True:
            try:
                sks = int(input("SKS: "))
                if 0 <= sks <= 24:
                    break
                print("SKS harus antara 0 sampai 24.")
            except ValueError:
                print("SKS harus berupa angka bulat.")

        data.append({
            "nim": nim,
            "nama": nama,
            "ipk": ipk,
            "sks": sks,
            "status": cek_status_mahasiswa(ipk, sks),
        })

    return data


def tampilkan_laporan(data: list[dict]) -> None:
    """Menampilkan laporan status mahasiswa."""
    print("\n=== LAPORAN STATUS MAHASISWA ===")
    print(f"{'NIM':<12} {'Nama':<20} {'IPK':>6} {'SKS':>5} {'Status':<12}")
    print("-" * 60)

    for item in data:
        print(f"{item['nim']:<12} {item['nama']:<20} {item['ipk']:>6.2f} {item['sks']:>5} {item['status']:<12}")


def main():
    mahasiswa = input_mahasiswa()
    tampilkan_laporan(mahasiswa)


if __name__ == "__main__":
    main()
