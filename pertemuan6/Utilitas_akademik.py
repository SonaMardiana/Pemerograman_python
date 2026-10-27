"""
Modul utilitas_akademik
Berisi fungsi untuk konversi nilai, perhitungan IPK, dan pembuatan transkrip.

Skala nilai (bisa disesuaikan dengan aturan kampus):
    >= 80 : A  (4.0)
    >= 75 : B+ (3.5)
    >= 70 : B  (3.0)
    >= 65 : C+ (2.5)
    >= 60 : C  (2.0)
    >= 50 : D  (1.0)
    <  50 : E  (0.0)
"""

# (batas_bawah, huruf, bobot) diurutkan dari yang tertinggi
SKALA_NILAI = [
    (80, "A", 4.0),
    (75, "B+", 3.5),
    (70, "B", 3.0),
    (65, "C+", 2.5),
    (60, "C", 2.0),
    (50, "D", 1.0),
    (0, "E", 0.0),
]


def konversi_nilai_huruf(nilai_angka):
    """
    Mengonversi nilai angka (0-100) menjadi tuple (huruf, bobot).

    Contoh:
        konversi_nilai_huruf(82) -> ("A", 4.0)
    """
    if isinstance(nilai_angka, bool) or not isinstance(nilai_angka, (int, float)):
        raise TypeError("Nilai harus berupa angka.")
    if not 0 <= nilai_angka <= 100:
        raise ValueError(f"Nilai harus antara 0 dan 100, didapat {nilai_angka}.")

    for batas, huruf, bobot in SKALA_NILAI:
        if nilai_angka >= batas:
            return huruf, bobot


def hitung_ipk(daftar_mk):
    """
    Menghitung IPK dari daftar mata kuliah.

    Parameter:
        daftar_mk: list of dict, tiap dict berisi
                   {"kode": str, "nama": str, "sks": int, "nilai": angka 0-100}

    Rumus: IPK = sum(sks * bobot) / sum(sks)
    Return: float (dibulatkan 2 desimal)
    """
    if not daftar_mk:
        raise ValueError("Daftar mata kuliah tidak boleh kosong.")

    total_sks = 0
    total_mutu = 0.0
    for mk in daftar_mk:
        sks = mk["sks"]
        if sks <= 0:
            raise ValueError(f"SKS '{mk['nama']}' harus lebih dari 0.")
        _, bobot = konversi_nilai_huruf(mk["nilai"])
        total_sks += sks
        total_mutu += sks * bobot

    return round(total_mutu / total_sks, 2)


def generate_transkrip(nama, nim, daftar_mk):
    """
    Membuat transkrip nilai dalam bentuk teks (string) yang siap dicetak.
    """
    lebar = 66
    garis = "=" * lebar
    pemisah = "-" * lebar

    baris = [
        garis,
        "TRANSKRIP NILAI".center(lebar),
        garis,
        f"Nama : {nama}",
        f"NIM  : {nim}",
        pemisah,
        f"{'No':<4}{'Kode':<10}{'Mata Kuliah':<26}{'SKS':>4}{'Nilai':>7}{'Huruf':>7}{'Bobot':>7}",
        pemisah,
    ]

    total_sks = 0
    for no, mk in enumerate(daftar_mk, start=1):
        huruf, bobot = konversi_nilai_huruf(mk["nilai"])
        total_sks += mk["sks"]
        baris.append(
            f"{no:<4}{mk['kode']:<10}{mk['nama'][:25]:<26}"
            f"{mk['sks']:>4}{mk['nilai']:>7}{huruf:>7}{bobot:>7.1f}"
        )

    ipk = hitung_ipk(daftar_mk)
    baris += [
        pemisah,
        f"Total SKS : {total_sks}",
        f"IPK       : {ipk:.2f}",
        garis,
    ]
    return "\n".join(baris)


if __name__ == "__main__":
    # Pengujian sederhana untuk modul ini
    print("=== Test konversi_nilai_huruf ===")
    for n in (95, 80, 77, 70, 66, 61, 55, 30):
        print(f"{n:>3} -> {konversi_nilai_huruf(n)}")

    data_uji = [
        {"kode": "IF101", "nama": "Algoritma", "sks": 3, "nilai": 85},
        {"kode": "IF102", "nama": "Basis Data", "sks": 3, "nilai": 72},
        {"kode": "MK103", "nama": "Matematika Diskrit", "sks": 2, "nilai": 66},
    ]

    print("\n=== Test hitung_ipk ===")
    # (3*4.0 + 3*3.0 + 2*2.5) / 8 = 26 / 8 = 3.25
    ipk = hitung_ipk(data_uji)
    print("IPK:", ipk)
    assert ipk == 3.25, "Perhitungan IPK salah!"

    print("\n=== Test generate_transkrip ===")
    print(generate_transkrip("Contoh Mahasiswa", "123456", data_uji))

    print("\n=== Test error handling ===")
    for fungsi, arg in ((konversi_nilai_huruf, 120), (hitung_ipk, [])):
        try:
            fungsi(arg)
        except ValueError as e:
            print("ValueError:", e)

    print("\nSemua test lulus.")