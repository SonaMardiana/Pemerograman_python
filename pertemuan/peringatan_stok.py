def evaluasi_stok(jumlah: int) -> str:
    """Menentukan status stok berdasarkan jumlah."""
    if jumlah >= 25:
        return "Aman"
    if jumlah >= 15:
        return "Peringatan"
    if jumlah >= 5:
        return "Rendah"
    return "Habis"


def prioritas_stok(status: str) -> str:
    """Menentukan prioritas berdasarkan status stok."""
    if status in {"Habis", "Rendah"}:
        return "Tinggi"
    if status == "Peringatan":
        return "Menengah"
    return "Rendah"


def data_inventaris() -> list[dict]:
    """Data inventaris contoh minimal 8 item."""
    return [
        {"kode": "A01", "nama": "Mouse", "stok": 30, "harga": 85000},
        {"kode": "A02", "nama": "Keyboard", "stok": 22, "harga": 180000},
        {"kode": "A03", "nama": "Monitor", "stok": 12, "harga": 1200000},
        {"kode": "A04", "nama": "Flashdisk", "stok": 0, "harga": 150000},
        {"kode": "A05", "nama": "RAM 8GB", "stok": 26, "harga": 350000},
        {"kode": "A06", "nama": "SSD 512GB", "stok": 18, "harga": 650000},
        {"kode": "A07", "nama": "Speaker", "stok": 4, "harga": 220000},
        {"kode": "A08", "nama": "Printer", "stok": 1, "harga": 1750000},
    ]


def tampilkan_laporan_stok(inventaris: list[dict]) -> None:
    """Menampilkan laporan lengkap stok."""
    print("\n=== LAPORAN PERINGATAN STOK ===")
    print(f"{'Kode':<8} {'Nama':<20} {'Stok':>6} {'Status':<12} {'Prioritas':<10} {'Nilai':>16}")
    print("-" * 80)

    total_nilai = 0
    statistik = {"Aman": 0, "Peringatan": 0, "Rendah": 0, "Habis": 0}

    for item in inventaris:
        status = evaluasi_stok(item["stok"])
        statistik[status] += 1
        nilai = item["stok"] * item["harga"]
        total_nilai += nilai

        print(f"{item['kode']:<8} {item['nama']:<20} {item['stok']:>6} {status:<12} {prioritas_stok(status):<10} Rp {nilai:>12,.0f}")

    total_item = len(inventaris)
    butuh_restock = statistik["Rendah"] + statistik["Habis"]
    persentase_restock = (butuh_restock / total_item) * 100 if total_item else 0

    print("\n=== RINGKASAN STATISTIK ===")
    print(f"Total item inventaris      : {total_item}")
    print(f"Aman                       : {statistik['Aman']}")
    print(f"Peringatan                 : {statistik['Peringatan']}")
    print(f"Rendah                     : {statistik['Rendah']}")
    print(f"Habis                      : {statistik['Habis']}")
    print(f"Total nilai inventaris     : Rp {total_nilai:,.0f}")
    print(f"Persentase perlu restock   : {persentase_restock:.2f}%")


def main():
    inventaris = data_inventaris()
    tampilkan_laporan_stok(inventaris)


if __name__ == "__main__":
    main()
