"""Validasi sederhana untuk data Mahasiswa."""


def validasi_mahasiswa(data: dict) -> None:
    """Memastikan field mahasiswa tersedia dan berupa teks non-kosong."""
    for field in ("nim", "nama", "jurusan"):
        nilai = data.get(field)
        if not isinstance(nilai, str) or not nilai.strip():
            raise ValueError(f"Field '{field}' wajib diisi dengan teks.")
