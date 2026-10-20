from collections import Counter
from pathlib import Path
import re


def analisis_teks(teks):
    kata = re.findall(r"\b\w+\b", teks.casefold())
    frekuensi = dict(Counter(kata))
    kata_teratas = sorted(frekuensi.items(), key=lambda item: (-item[1], item[0]))[:10]
    hapax = sorted(kata_unik for kata_unik, jumlah in frekuensi.items() if jumlah == 1)
    rasio = len(set(kata)) / len(kata) if kata else 0
    return kata, frekuensi, kata_teratas, hapax, rasio


def main():
    berkas_default = Path(__file__).with_name("teks.txt")
    masukan = input(
        f"Masukkan path file teks (Enter untuk {berkas_default.name}): "
    ).strip()
    path_berkas = Path(masukan) if masukan else berkas_default

    try:
        teks = path_berkas.read_text(encoding="utf-8")
    except OSError as error:
        print(f"Tidak dapat membaca file '{path_berkas}': {error}")
        return

    kata, frekuensi, kata_teratas, hapax, rasio = analisis_teks(teks)
    print(f"Jumlah total kata: {len(kata)}")
    print(f"Frekuensi setiap kata: {frekuensi}")
    print("10 kata paling sering muncul:")
    for kata_teratas_item, jumlah in kata_teratas:
        print(f"  {kata_teratas_item}: {jumlah}")
    print(f"Kata yang hanya muncul sekali (hapax legomena): {hapax}")
    print(f"Type-token ratio: {rasio:.4f}")


if __name__ == "__main__":
    main()
