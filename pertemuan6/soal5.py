"""Mengambil dan menganalisis data posts dari JSONPlaceholder."""

import json
from pathlib import Path

import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"
FILE_HASIL = Path(__file__).with_name("hasil_soal5.json")


def main():
    """Ambil posts, proses dengan map/filter/sorted, lalu simpan ke JSON."""
    print("Mengambil data dari JSONPlaceholder...")
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()
    posts = response.json()

    # map + lambda: pilih data yang diperlukan dan hitung jumlah kata.
    posts_ringkas = list(
        map(
            lambda post: {
                "id": post["id"],
                "userId": post["userId"],
                "judul": post["title"],
                "jumlah_kata": len(post["body"].split()),
            },
            posts,
        )
    )

    # filter + lambda: simpan post yang judulnya lebih dari 50 karakter.
    posts_terpilih = list(
        filter(lambda post: len(post["judul"]) > 50, posts_ringkas)
    )

    # sorted + lambda: urutkan post terpilih berdasarkan judul.
    posts_urut = sorted(posts_terpilih, key=lambda post: post["judul"].lower())

    total_kata = sum(map(lambda post: post["jumlah_kata"], posts_urut))
    hasil = {
        "sumber": API_URL,
        "jumlah_data_api": len(posts),
        "kriteria_filter": "Panjang judul lebih dari 50 karakter",
        "jumlah_data_terpilih": len(posts_urut),
        "total_kata_pada_data_terpilih": total_kata,
        "rata_rata_kata_per_post": round(total_kata / len(posts_urut), 2)
        if posts_urut
        else 0,
        "posts": posts_urut,
    }

    FILE_HASIL.write_text(
        json.dumps(hasil, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Selesai. {len(posts)} data diambil dari API.")
    print(f"{len(posts_urut)} data lolos filter dan diurutkan berdasarkan judul.")
    print(f"Hasil disimpan ke: {FILE_HASIL}")


if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.RequestException as error:
        print(f"Gagal mengambil data dari API: {error}")
    except (KeyError, TypeError, ValueError) as error:
        print(f"Format data dari API tidak sesuai: {error}")
