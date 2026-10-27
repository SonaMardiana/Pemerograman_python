"""Struktur data entitas Mahasiswa."""

from typing import TypedDict


class Mahasiswa(TypedDict):
    """Data mahasiswa yang disimpan sebagai dictionary."""

    nim: str
    nama: str
    jurusan: str
