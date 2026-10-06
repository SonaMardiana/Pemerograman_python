def hitung_persentase_mahasiswa(data: list[dict]) -> tuple[float, float]:
    """Menghitung persentase mahasiswa aktif dan tidak aktif."""
    total = len(data)
    if total == 0:
        return 0.0, 0.0

    aktif = sum(1 for item in data if item.get("status") == "Aktif")
    tidak_aktif = sum(1 for item in data if item.get("status") == "Tidak Aktif")

    return (aktif / total) * 100, (tidak_aktif / total) * 100


def rata_rata_diskon(data: list[dict]) -> float:
    """Menghitung rata-rata diskon yang diberikan."""
    if not data:
        return 0.0
    return sum(item.get("diskon_total", 0) for item in data) / len(data)


def persentase_perlu_restock(data: list[dict]) -> float:
    """Menghitung persentase item yang perlu restock."""
    total = len(data)
    if total == 0:
        return 0.0

    perlu_restock = sum(1 for item in data if item.get("status") in {"Rendah", "Habis"})
    return (perlu_restock / total) * 100


def tampilkan_tabel_ringkasan(aktif_persen: float, tidak_aktif_persen: float, rata_diskon: float, restock_persen: float) -> None:
    """Menampilkan ringkasan dalam format tabel sederhana."""
    print("\n=== RINGKASAN ALGORITMA ===")
    print(f"{'Aspek':<25} {'Hasil':>12}")
    print("-" * 40)
    print(f"{'Mahasiswa Aktif':<25} {aktif_persen:>10.2f}%")
    print(f"{'Mahasiswa Tidak Aktif':<25} {tidak_aktif_persen:>10.2f}%")
    print(f"{'Rata-rata Diskon':<25} {rata_diskon * 100:>10.2f}%")
    print(f"{'Item Perlu Restock':<25} {restock_persen:>10.2f}%")


def main():
    mahasiswa = [
        {"status": "Aktif"},
        {"status": "Aktif"},
        {"status": "Peringatan"},
        {"status": "Tidak Aktif"},
        {"status": "Aktif"},
    ]

    diskon = [
        {"diskon_total": 0.25},
        {"diskon_total": 0.10},
        {"diskon_total": 0.40},
        {"diskon_total": 0.15},
        {"diskon_total": 0.30},
    ]

    stok = [
        {"status": "Aman"},
        {"status": "Peringatan"},
        {"status": "Rendah"},
        {"status": "Habis"},
        {"status": "Aman"},
        {"status": "Peringatan"},
        {"status": "Rendah"},
    ]

    aktif_persen, tidak_aktif_persen = hitung_persentase_mahasiswa(mahasiswa)
    rata_diskon_total = rata_rata_diskon(diskon)
    restock_persen = persentase_perlu_restock(stok)

    tampilkan_tabel_ringkasan(aktif_persen, tidak_aktif_persen, rata_diskon_total, restock_persen)


if __name__ == "__main__":
    main()
