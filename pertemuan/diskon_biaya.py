def hitung_diskon_biaya(spp: float, anak_karyawan: str, ipk: float, tepat_waktu: str) -> dict:
    """Menghitung diskon, potongan, dan biaya final."""
    anak_karyawan = anak_karyawan.strip().lower() == "y"
    tepat_waktu = tepat_waktu.strip().lower() == "y"

    diskon_total = 0.0

    if anak_karyawan:
        diskon_total += 0.25
    if ipk >= 3.8:
        diskon_total += 0.20
    elif ipk >= 3.5:
        diskon_total += 0.15
    elif ipk >= 3.0:
        diskon_total += 0.10
    if tepat_waktu:
        diskon_total += 0.05

    if diskon_total > 0.95:
        diskon_total = 0.95

    potongan = spp * diskon_total
    biaya_final = spp - potongan

    return {
        "diskon_total": diskon_total,
        "potongan": potongan,
        "biaya_final": biaya_final,
    }


def input_data_diskon() -> dict:
    """Menerima input data biaya kuliah."""
    while True:
        try:
            spp = float(input("Biaya SPP: ").replace(",", "."))
            if spp > 0:
                break
            print("Biaya SPP harus lebih dari 0.")
        except ValueError:
            print("Biaya SPP harus berupa angka.")

    while True:
        anak_karyawan = input("Status anak karyawan (y/n): ").strip().lower()
        if anak_karyawan in {"y", "n"}:
            break
        print("Jawaban harus y atau n.")

    while True:
        try:
            ipk = float(input("IPK: ").replace(",", "."))
            if 0.0 <= ipk <= 4.0:
                break
            print("IPK harus antara 0.0 sampai 4.0.")
        except ValueError:
            print("IPK harus berupa angka.")

    while True:
        tepat_waktu = input("Pembayaran tepat waktu (y/n): ").strip().lower()
        if tepat_waktu in {"y", "n"}:
            break
        print("Jawaban harus y atau n.")

    return {
        "spp": spp,
        "anak_karyawan": anak_karyawan,
        "ipk": ipk,
        "tepat_waktu": tepat_waktu,
    }


def tampilkan_hasil_diskon(data: dict) -> None:
    """Menampilkan hasil perhitungan diskon."""
    hasil = hitung_diskon_biaya(data["spp"], data["anak_karyawan"], data["ipk"], data["tepat_waktu"])
    print("\n=== HASIL KALKULASI DISKON ===")
    print(f"Biaya SPP      : Rp {data['spp']:,.2f}")
    print(f"Diskon total   : {hasil['diskon_total'] * 100:.2f}%")
    print(f"Potongan       : Rp {hasil['potongan']:,.2f}")
    print(f"Biaya final    : Rp {hasil['biaya_final']:,.2f}")


def main():
    data = input_data_diskon()
    tampilkan_hasil_diskon(data)


if __name__ == "__main__":
    main()
