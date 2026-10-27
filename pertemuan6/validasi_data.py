"""
Praktikum: Fungsi validasi_data()
Memvalidasi dictionary data berdasarkan schema (tipe dan rentang).
"""


def validasi_data(data, schema, *args, **kwargs):
    """
    Memvalidasi dictionary `data` terhadap `schema`.

    Format schema (per field):
        {
            "nama_field": {
                "tipe": int,        # tipe data (boleh tuple, mis. (int, float))
                "min": 0,           # nilai minimum (angka) / panjang minimum (str, list)
                "max": 100,         # nilai maksimum (angka) / panjang maksimum (str, list)
                "wajib": True,      # default True; False = boleh tidak ada
            }
        }

    *args (fleksibel):
        - dict     -> schema tambahan, digabung ke schema utama
        - callable -> fungsi validator kustom: f(data) -> None / str / list[str]
                      (mengembalikan pesan error jika data tidak valid)

    **kwargs (opsi):
        - strict (bool, default False)          : field yang tidak ada di schema dianggap error
        - berhenti_pertama (bool, default False): berhenti setelah error pertama ditemukan

    Return:
        tuple (is_valid: bool, errors: list[str])
    """
    strict = kwargs.get("strict", False)
    berhenti_pertama = kwargs.get("berhenti_pertama", False)

    errors = []

    # Gabungkan schema tambahan dan kumpulkan validator kustom dari *args
    schema_gabungan = dict(schema)
    validator_kustom = []
    for arg in args:
        if isinstance(arg, dict):
            schema_gabungan.update(arg)
        elif callable(arg):
            validator_kustom.append(arg)
        else:
            raise TypeError(
                f"Argumen tambahan harus dict atau fungsi, bukan {type(arg).__name__}"
            )

    def tambah_error(pesan):
        errors.append(pesan)
        return berhenti_pertama  # True -> minta berhenti

    # 1. Validasi tiap field di schema
    for field, aturan in schema_gabungan.items():
        wajib = aturan.get("wajib", True)

        if field not in data:
            if wajib and tambah_error(f"'{field}': field wajib diisi"):
                return False, errors
            continue  # field tidak ada -> tidak ada yang perlu dicek lagi

        nilai = data[field]

        # Cek tipe
        tipe = aturan.get("tipe")
        if tipe is not None:
            # bool adalah subclass int di Python, jadi tolak bool jika diminta int/float
            tipe_tuple = tipe if isinstance(tipe, tuple) else (tipe,)
            bool_salah = isinstance(nilai, bool) and bool not in tipe_tuple
            if bool_salah or not isinstance(nilai, tipe_tuple):
                nama_tipe = " / ".join(t.__name__ for t in tipe_tuple)
                if tambah_error(
                    f"'{field}': tipe harus {nama_tipe}, bukan {type(nilai).__name__}"
                ):
                    return False, errors
                continue  # tipe salah, rentang tidak perlu dicek

        # Cek rentang (angka -> nilainya, str/list/tuple/dict -> panjangnya)
        if isinstance(nilai, (int, float)) and not isinstance(nilai, bool):
            ukuran, label = nilai, "nilai"
        elif isinstance(nilai, (str, list, tuple, dict)):
            ukuran, label = len(nilai), "panjang"
        else:
            ukuran = None

        if ukuran is not None:
            if "min" in aturan and ukuran < aturan["min"]:
                if tambah_error(
                    f"'{field}': {label} minimal {aturan['min']}, didapat {ukuran}"
                ):
                    return False, errors
            if "max" in aturan and ukuran > aturan["max"]:
                if tambah_error(
                    f"'{field}': {label} maksimal {aturan['max']}, didapat {ukuran}"
                ):
                    return False, errors

    # 2. Mode strict: tolak field di luar schema
    if strict:
        for field in data:
            if field not in schema_gabungan:
                if tambah_error(f"'{field}': field tidak dikenal di schema"):
                    return False, errors

    # 3. Jalankan validator kustom dari *args
    for fungsi in validator_kustom:
        hasil = fungsi(data)
        if hasil:
            pesan_list = [hasil] if isinstance(hasil, str) else list(hasil)
            for pesan in pesan_list:
                if tambah_error(pesan):
                    return False, errors

    return len(errors) == 0, errors


if __name__ == "__main__":
    schema_mhs = {
        "nama": {"tipe": str, "min": 3, "max": 50},
        "umur": {"tipe": int, "min": 17, "max": 60},
        "ipk": {"tipe": (int, float), "min": 0.0, "max": 4.0},
        "email": {"tipe": str, "wajib": False},
    }

    # Contoh 1: data valid
    data1 = {"nama": "Sona", "umur": 20, "ipk": 3.75}
    print("Contoh 1:", validasi_data(data1, schema_mhs))

    # Contoh 2: banyak error sekaligus
    data2 = {"nama": "Al", "umur": "dua puluh", "ipk": 4.5}
    print("Contoh 2:", validasi_data(data2, schema_mhs))

    # Contoh 3: field wajib hilang
    data3 = {"nama": "Budi"}
    print("Contoh 3:", validasi_data(data3, schema_mhs))

    # Contoh 4: **kwargs -> strict + berhenti_pertama
    data4 = {"nama": "Sona", "umur": 20, "ipk": 3.5, "alamat": "Bandung"}
    print("Contoh 4:", validasi_data(data4, schema_mhs, strict=True))
    print("Contoh 4b:", validasi_data(data2, schema_mhs, berhenti_pertama=True))

    # Contoh 5: *args -> schema tambahan + validator kustom
    schema_tambahan = {"semester": {"tipe": int, "min": 1, "max": 14}}

    def cek_email_ada_at(data):
        email = data.get("email")
        if email is not None and "@" not in email:
            return "'email': format tidak valid (tidak ada '@')"

    data5 = {"nama": "Sona", "umur": 20, "ipk": 3.5, "semester": 20, "email": "sona.com"}
    print("Contoh 5:", validasi_data(data5, schema_mhs, schema_tambahan, cek_email_ada_at))