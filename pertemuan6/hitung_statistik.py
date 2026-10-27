"""
Praktikum: Fungsi hitung_statistik()
Hanya menggunakan standard library (statistics, math).
"""

import math
import statistics


def hitung_statistik(data, sampel=True):
    """
    Menghitung statistik deskriptif dari sebuah list angka.

    Parameter:
        data  : list/tuple berisi angka (int atau float)
        sampel: True  -> standar deviasi sampel (pembagi n-1)
                False -> standar deviasi populasi (pembagi n)

    Return:
        dict dengan key: mean, median, modus, range, std_dev
        (modus berupa list, karena bisa ada lebih dari satu nilai modus)
    """
    if not data:
        raise ValueError("List tidak boleh kosong.")

    n = len(data)

    mean = statistics.mean(data)
    median = statistics.median(data)
    modus = statistics.multimode(data)   # list semua nilai yang paling sering muncul
    rentang = max(data) - min(data)

    # Standar deviasi = akar dari varians
    if sampel:
        # Varians sampel butuh minimal 2 data
        varians = statistics.variance(data) if n > 1 else 0.0
    else:
        varians = statistics.pvariance(data)
    std_dev = math.sqrt(varians)

    return {
        "mean": mean,
        "median": median,
        "modus": modus,
        "range": rentang,
        "std_dev": std_dev,
    }


if __name__ == "__main__":
    # Contoh 1: data dengan satu modus
    data1 = [4, 8, 6, 5, 3, 8, 9, 7, 8, 5]
    hasil1 = hitung_statistik(data1)
    print("Data   :", data1)
    for kunci, nilai in hasil1.items():
        if isinstance(nilai, float):
            print(f"{kunci:8}: {nilai:.4f}")
        else:
            print(f"{kunci:8}: {nilai}")

    print()

    # Contoh 2: data dengan modus ganda
    data2 = [1, 2, 2, 3, 3, 4]
    hasil2 = hitung_statistik(data2, sampel=False)  # standar deviasi populasi
    print("Data   :", data2)
    for kunci, nilai in hasil2.items():
        if isinstance(nilai, float):
            print(f"{kunci:8}: {nilai:.4f}")
        else:
            print(f"{kunci:8}: {nilai}")

    print()

    # Contoh 3: list kosong -> error
    try:
        hitung_statistik([])
    except ValueError as e:
        print("Error  :", e)