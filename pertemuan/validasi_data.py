def validasi_mahasiswa_data(nim: str, ipk: float, sks: int, semester: int) -> list[str]:
    """Validasi data mahasiswa dan mengembalikan list error."""
    errors = []

    if not nim or not nim.isdigit() or len(nim) != 10:
        errors.append("NIM harus 10 digit angka.")
    else:
        tahun = int(nim[:4])
        if not (2000 <= tahun <= 2037):
            errors.append("Tahun pada NIM harus 2000-2037.")

    if not (0.0 <= ipk <= 4.0):
        errors.append("IPK harus berada dalam rentang 0.0-4.0.")

    if not (0 <= sks <= 24):
        errors.append("SKS harus berada dalam rentang 0-24.")

    if not (1 <= semester <= 14):
        errors.append("Semester harus berada dalam rentang 1-14.")

    return errors


def main():
    print("=== VALIDASI DATA MAHASISWA ===")
    nim = input("NIM (10 digit): ").strip()

    try:
        ipk = float(input("IPK: ").replace(",", "."))
    except ValueError:
        ipk = -1.0

    try:
        sks = int(input("SKS: "))
    except ValueError:
        sks = -1

    try:
        semester = int(input("Semester: "))
    except ValueError:
        semester = -1

    errors = validasi_mahasiswa_data(nim, ipk, sks, semester)

    if errors:
        print("\nData tidak valid:")
        for error in errors:
            print(f"- {error}")
    else:
        print("\nData mahasiswa valid.")


if __name__ == "__main__":
    main()
