"""Layanan untuk mengelola data sistem informasi."""

from .mahasiswa_service import (
    hapus_mahasiswa,
    tambah_mahasiswa,
    ubah_mahasiswa,
    lihat_mahasiswa,
    lihat_semua_mahasiswa,
)

__all__ = [
    "tambah_mahasiswa",
    "lihat_mahasiswa",
    "lihat_semua_mahasiswa",
    "ubah_mahasiswa",
    "hapus_mahasiswa",
]
