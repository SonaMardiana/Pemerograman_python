"""Contoh penggunaan CRUD dari package sistem_informasi."""

from sistem_informasi import (
    hapus_mahasiswa,
    tambah_mahasiswa,
    ubah_mahasiswa,
    lihat_mahasiswa,
    lihat_semua_mahasiswa,
)


if __name__ == "__main__":
    tambah_mahasiswa("230001", "Sona", "Informatika")
    tambah_mahasiswa("230002", "Budi", "Sistem Informasi")
    print("Semua mahasiswa:", lihat_semua_mahasiswa())

    ubah_mahasiswa("230001", jurusan="Teknik Informatika")
    print("Setelah diubah:", lihat_mahasiswa("230001"))

    hapus_mahasiswa("230002")
    print("Setelah dihapus:", lihat_semua_mahasiswa())
