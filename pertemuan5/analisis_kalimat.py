def main():
    kalimat = input("Masukkan sebuah kalimat: ")
    kata = kalimat.split()

    print(f"Jumlah kata: {len(kata)}")
    print(f"Jumlah karakter (termasuk spasi): {len(kalimat)}")
    if kata:
        print(f"Kata terpanjang: {max(kata, key=len)}")
    else:
        print("Kata terpanjang: tidak ada")
    print(f"Kalimat dalam title case: {kalimat.title()}")


if __name__ == "__main__":
    main()
