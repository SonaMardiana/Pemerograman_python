def baca_id(prompt):
    masukan = input(prompt).strip()
    return {item.strip() for item in masukan.split(",") if item.strip()}


def main():
    beasiswa_a = baca_id("Masukkan ID penerima beasiswa A (pisahkan dengan koma): ")
    beasiswa_b = baca_id("Masukkan ID penerima beasiswa B (pisahkan dengan koma): ")

    print(f"Menerima kedua beasiswa: {sorted(beasiswa_a & beasiswa_b)}")
    print(f"Hanya menerima beasiswa A: {sorted(beasiswa_a - beasiswa_b)}")
    print(f"Menerima beasiswa B tapi tidak A: {sorted(beasiswa_b - beasiswa_a)}")
    print(f"Semua penerima unik: {sorted(beasiswa_a | beasiswa_b)}")


if __name__ == "__main__":
    main()
