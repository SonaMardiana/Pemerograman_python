KATEGORI_NILAI = ("A", "B", "C", "D", "E")


def tentukan_kategori(nilai):
    if nilai >= 80:
        return "A"
    if nilai >= 70:
        return "B"
    if nilai >= 60:
        return "C"
    if nilai >= 50:
        return "D"
    return "E"


def main():
    masukan = input("Masukkan nilai mahasiswa, pisahkan dengan koma: ")
    try:
        nilai_mahasiswa = [float(nilai.strip()) for nilai in masukan.split(",")]
    except ValueError:
        print("Masukan tidak valid. Gunakan angka yang dipisahkan dengan koma.")
        return

    if not nilai_mahasiswa or any(not 0 <= nilai <= 100 for nilai in nilai_mahasiswa):
        print("Masukkan setidaknya satu nilai dalam rentang 0 sampai 100.")
        return

    kelompok = {kategori: [] for kategori in KATEGORI_NILAI}
    for nilai in nilai_mahasiswa:
        kelompok[tentukan_kategori(nilai)].append(nilai)

    frekuensi = {kategori: len(nilai) for kategori, nilai in kelompok.items()}
    print(f"Rata-rata: {sum(nilai_mahasiswa) / len(nilai_mahasiswa):.2f}")
    print(f"Nilai tertinggi: {max(nilai_mahasiswa):g}")
    print(f"Nilai terendah: {min(nilai_mahasiswa):g}")
    print("Pengelompokan nilai:")
    for kategori, nilai in kelompok.items():
        print(f"  {kategori}: {nilai}")
    print(f"Frekuensi kategori: {frekuensi}")


if __name__ == "__main__":
    main()
