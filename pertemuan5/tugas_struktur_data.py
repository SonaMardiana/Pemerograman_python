"""Tugas Struktur Data Python (soal 1-5 dalam satu file).

Jalankan: python tugas_struktur_data.py
"""
import re
import string


# ======================================================================
# SOAL 1: Analisis kalimat
# ======================================================================
def analisis_kalimat(kalimat):
    daftar_kata = kalimat.split()
    kata_bersih = [k.strip(string.punctuation) for k in daftar_kata]
    terpanjang = max(kata_bersih, key=len) if kata_bersih else ""
    title = " ".join(k.capitalize() for k in daftar_kata)
    return {
        "jumlah_kata": len(daftar_kata),
        "jumlah_karakter": len(kalimat),
        "karakter_tanpa_spasi": len(kalimat.replace(" ", "")),
        "kata_terpanjang": terpanjang,
        "title_case": title,
    }


def soal1():
    print("\n=== SOAL 1: Analisis Kalimat ===")
    kalimat = input("Masukkan sebuah kalimat: ")
    h = analisis_kalimat(kalimat)
    print(f"(a) Jumlah kata              : {h['jumlah_kata']}")
    print(f"(b) Jumlah karakter          : {h['jumlah_karakter']} "
          f"(tanpa spasi: {h['karakter_tanpa_spasi']})")
    print(f"(c) Kata terpanjang          : {h['kata_terpanjang']!r}")
    print(f"(d) Title case               : {h['title_case']}")


# ======================================================================
# SOAL 2: Analisis nilai mahasiswa
# ======================================================================
def kategori(nilai):
    if nilai >= 85:
        return "A"
    if nilai >= 70:
        return "B"
    if nilai >= 60:
        return "C"
    if nilai >= 50:
        return "D"
    return "E"


def analisis_nilai(daftar_nilai):
    frekuensi = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for n in daftar_nilai:
        frekuensi[kategori(n)] += 1
    return (sum(daftar_nilai) / len(daftar_nilai),
            max(daftar_nilai), min(daftar_nilai), frekuensi)


def soal2():
    print("\n=== SOAL 2: Analisis Nilai Mahasiswa ===")
    teks = input("Masukkan nilai (pisahkan dengan spasi/koma): ")
    try:
        nilai = [float(x) for x in teks.replace(",", " ").split()]
    except ValueError:
        print("Input tidak valid: hanya angka yang diperbolehkan.")
        return
    if not nilai:
        print("Daftar nilai kosong.")
        return
    rata, tinggi, rendah, frek = analisis_nilai(nilai)
    print(f"(a) Rata-rata       : {rata:.2f}")
    print(f"(b) Tertinggi       : {tinggi:g}")
    print(f"    Terendah        : {rendah:g}")
    print("(c) Kategori        : " + ", ".join(f"{n:g}={kategori(n)}" for n in nilai))
    print(f"(d) Frekuensi       : {frek}")


# ======================================================================
# SOAL 3: Operasi set beasiswa
# ======================================================================
def soal3():
    print("\n=== SOAL 3: Operasi Set Beasiswa ===")
    beasiswa_a = ["M001", "M002", "M003", "M004", "M005", "M003"]
    beasiswa_b = ["M004", "M005", "M006", "M007", "M002"]
    a, b = set(beasiswa_a), set(beasiswa_b)
    print(f"Beasiswa A: {beasiswa_a}")
    print(f"Beasiswa B: {beasiswa_b}")
    print(f"(a) Menerima keduanya : {sorted(a & b)}")
    print(f"(b) Hanya A           : {sorted(a - b)}")
    print(f"(c) B tapi bukan A    : {sorted(b - a)}")
    print(f"(d) Semua unik        : {sorted(a | b)}")


# ======================================================================
# SOAL 4: Inventaris toko {nama: (harga, stok)}
# ======================================================================
def tambah_barang(inv, nama, harga, stok):
    nama = nama.lower()
    if nama in inv:
        return False
    if harga < 0 or stok < 0:
        raise ValueError("Harga dan stok tidak boleh negatif.")
    inv[nama] = (harga, stok)
    return True


def update_stok(inv, nama, stok_baru):
    nama = nama.lower()
    if nama not in inv:
        return False
    if stok_baru < 0:
        raise ValueError("Stok tidak boleh negatif.")
    harga, _ = inv[nama]
    inv[nama] = (harga, stok_baru)  # tuple immutable -> buat ulang
    return True


def cari_by_harga(inv, harga_min, harga_max):
    return {n: (h, s) for n, (h, s) in inv.items() if harga_min <= h <= harga_max}


def total_nilai(inv):
    return sum(h * s for h, s in inv.values())


def tampil_inventaris(inv):
    for nama, (harga, stok) in inv.items():
        print(f"    {nama:<12} Rp{harga:>9,}  stok: {stok}")


def soal4():
    print("\n=== SOAL 4: Inventaris Toko ===")
    inv = {
        "pensil": (2500, 100),
        "buku tulis": (8000, 50),
        "penghapus": (1500, 80),
        "tas ransel": (150000, 10),
    }
    print("Inventaris awal:")
    tampil_inventaris(inv)
    print("(a) Tambah 'spidol'        :", tambah_barang(inv, "spidol", 7000, 30))
    print("    Tambah 'pensil' (ada)  :", tambah_barang(inv, "pensil", 3000, 5))
    print("(b) Update stok 'pensil'=120:", update_stok(inv, "pensil", 120))
    print("    Update 'laptop' (tidak ada):", update_stok(inv, "laptop", 5))
    print("(c) Harga Rp2.000 - Rp10.000:")
    tampil_inventaris(cari_by_harga(inv, 2000, 10000))
    print(f"(d) Total nilai inventaris : Rp{total_nilai(inv):,}")


# ======================================================================
# SOAL 5: Frekuensi kata dari file
# ======================================================================
def baca_kata(path):
    with open(path, encoding="utf-8") as f:
        teks = f.read().lower()
    return re.findall(r"[a-zA-ZÀ-ɏ']+", teks)


def hitung_frekuensi(daftar_kata):
    frekuensi = {}
    for kata in daftar_kata:
        frekuensi[kata] = frekuensi.get(kata, 0) + 1
    return frekuensi


def top_n(frekuensi, n=10):
    return sorted(frekuensi.items(), key=lambda x: (-x[1], x[0]))[:n]


def hapax(frekuensi):
    return {k for k, v in frekuensi.items() if v == 1}


def type_token_ratio(daftar_kata):
    return len(set(daftar_kata)) / len(daftar_kata) if daftar_kata else 0.0


def soal5():
    print("\n=== SOAL 5: Frekuensi Kata dari File ===")
    path = input("Nama file teks (mis. teks_contoh.txt): ").strip()
    try:
        kata = baca_kata(path)
    except FileNotFoundError:
        print(f"File '{path}' tidak ditemukan.")
        return
    if not kata:
        print("File tidak berisi kata.")
        return
    frek = hitung_frekuensi(kata)
    print(f"Total kata: {len(kata)} | Kata unik: {len(frek)}")
    print(f"(a) Frekuensi tiap kata:\n    {frek}")
    print("(b) 10 kata teratas:")
    for i, (k, v) in enumerate(top_n(frek), 1):
        print(f"    {i:>2}. {k:<15} {v}")
    h = hapax(frek)
    print(f"(c) Hapax legomena ({len(h)}): {sorted(h)}")
    print(f"(d) Type-token ratio: {len(frek)}/{len(kata)} = "
          f"{type_token_ratio(kata):.4f}")


# ======================================================================
# MENU
# ======================================================================
def main():
    menu = {"1": soal1, "2": soal2, "3": soal3, "4": soal4, "5": soal5}
    while True:
        print("\n===== MENU TUGAS STRUKTUR DATA =====")
        print("1. Analisis kalimat")
        print("2. Analisis nilai mahasiswa")
        print("3. Operasi set beasiswa")
        print("4. Inventaris toko")
        print("5. Frekuensi kata dari file")
        print("0. Keluar")
        pilihan = input("Pilih (0-5): ").strip()
        if pilihan == "0":
            print("Selesai.")
            break
        fungsi = menu.get(pilihan)
        if fungsi:
            fungsi()
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
