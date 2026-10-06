# Sim Mahasiswa

Sistem Informasi Mahasiswa (SIM) adalah proyek aplikasi berbasis Python yang digunakan untuk mengelola data mahasiswa secara sederhana melalui antarmuka command line (CLI).

Aplikasi ini dibuat untuk latihan pengelolaan data menggunakan konsep class, validasi data, dan operasi dasar CRUD pada objek mahasiswa.

## Fitur

- Menambahkan data mahasiswa baru
- Menampilkan seluruh data mahasiswa dalam bentuk tabel
- Validasi NIM dan IPK
- Mencegah duplikasi NIM
- Struktur data mahasiswa yang mudah dikembangkan

## Teknologi

- Python 3
- Rich (untuk tampilan antarmuka terminal yang lebih rapi)
- Pytest (untuk pengujian unit)

## Struktur Proyek

```text
sim-mahasiswa/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── README.md
├── requirements.txt
├── myenv/
└── docs/
```

## Prasyarat

Pastikan Anda sudah memiliki:

- Python 3.10+ terinstal
- pip atau package manager Python
- Virtual environment (opsional, tetapi disarankan)

## Checklist Setup

Berikut checklist yang bisa Anda lakukan sebelum menjalankan proyek:

- [ ] Python sudah terinstal dan bisa diakses dari terminal
- [ ] Folder proyek sudah dibuka di workspace
- [ ] Virtual environment sudah dibuat atau tersedia
- [ ] Virtual environment sudah diaktifkan
- [ ] Dependensi sudah diinstal via `pip install -r requirements.txt`
- [ ] Pengujian sudah dijalankan dengan `pytest -q`
- [ ] Aplikasi sudah bisa dijalankan dengan `python src/main.py`

## Instalasi

1. Buka terminal di folder proyek.
2. Aktifkan virtual environment jika sudah ada:

```bash
myenv\Scripts\activate
```

3. Install dependency yang diperlukan:

```bash
pip install -r requirements.txt
```

## Menjalankan Aplikasi

Jalankan file utama berikut:

```bash
python src/main.py
```

Atau jika Anda menggunakan lingkungan virtual aktif:

```bash
python src/main.py
```

Setelah aplikasi berjalan, Anda akan melihat menu utama seperti:

- Tambah Mahasiswa
- Tampilkan Semua Mahasiswa
- Cari Mahasiswa (NIM)
- Hapus Mahasiswa
- Keluar

## Contoh Data Mahasiswa

Data mahasiswa yang diinput biasanya terdiri dari:

- NIM
- Nama
- Program Studi
- Angkatan
- IPK

Contoh:

```text
NIM: 2024SI001
Nama: Andi Pratama
Program Studi: Sistem Informasi
Angkatan: 2024
IPK: 3.50
```

## Validasi yang Diterapkan

- NIM harus diisi dan minimal memiliki panjang 6 karakter
- Nama tidak boleh kosong
- IPK harus berada dalam rentang 0.0 sampai 4.0
- NIM tidak boleh duplikat dalam daftar mahasiswa

## Testing

Untuk menjalankan pengujian unit:

```bash
pytest -q
```

## Catatan

Project ini masih bersifat pembelajaran dan dapat dikembangkan lebih lanjut, misalnya:

- fitur pencarian mahasiswa berdasarkan NIM
- fitur hapus mahasiswa
- penyimpanan data ke file JSON atau database
- antarmuka GUI atau web

## Kontribusi

Proyek ini dapat dikembangkan lebih lanjut sesuai kebutuhan pembelajaran atau tugas kuliah.

## Lisensi

Project ini dibuat untuk kebutuhan latihan dan penggunaan internal.
