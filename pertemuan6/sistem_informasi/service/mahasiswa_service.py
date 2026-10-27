"""Operasi CRUD Mahasiswa dengan penyimpanan dictionary in-memory."""

from ..model import Mahasiswa
from ..utils.validasi import validasi_mahasiswa

# Penyimpanan sementara: key adalah NIM, value adalah data mahasiswa.
_data_mahasiswa: dict[str, Mahasiswa] = {}


def tambah_mahasiswa(nim: str, nama: str, jurusan: str) -> Mahasiswa:
    """Menambahkan mahasiswa baru dan mengembalikan datanya."""
    data = {"nim": nim, "nama": nama, "jurusan": jurusan}
    validasi_mahasiswa(data)
    if nim in _data_mahasiswa:
        raise ValueError(f"Mahasiswa dengan NIM {nim} sudah ada.")

    _data_mahasiswa[nim] = data
    return data.copy()


def lihat_mahasiswa(nim: str) -> Mahasiswa:
    """Mengambil satu mahasiswa berdasarkan NIM."""
    if nim not in _data_mahasiswa:
        raise KeyError(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
    return _data_mahasiswa[nim].copy()


def lihat_semua_mahasiswa() -> list[Mahasiswa]:
    """Mengambil seluruh data mahasiswa."""
    return [mahasiswa.copy() for mahasiswa in _data_mahasiswa.values()]


def ubah_mahasiswa(nim: str, **perubahan: str) -> Mahasiswa:
    """Mengubah nama atau jurusan mahasiswa berdasarkan NIM."""
    if nim not in _data_mahasiswa:
        raise KeyError(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

    field_diizinkan = {"nama", "jurusan"}
    field_tidak_valid = set(perubahan) - field_diizinkan
    if field_tidak_valid:
        daftar = ", ".join(sorted(field_tidak_valid))
        raise ValueError(f"Field yang tidak dapat diubah: {daftar}.")

    data_baru = {**_data_mahasiswa[nim], **perubahan}
    validasi_mahasiswa(data_baru)
    _data_mahasiswa[nim] = data_baru
    return data_baru.copy()


def hapus_mahasiswa(nim: str) -> Mahasiswa:
    """Menghapus mahasiswa berdasarkan NIM dan mengembalikan datanya."""
    if nim not in _data_mahasiswa:
        raise KeyError(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
    return _data_mahasiswa.pop(nim)
