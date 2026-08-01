📊 Simulasi Optimasi Program Linier - Metode Grafis

Program simulasi untuk menyelesaikan masalah Program Linier 2 variabel dengan Metode Grafis (Geometris).

Mata Kuliah: Riset Operasional Materi: Pertemuan 2 - Program Linier dan Metode Grafis

🎯 Fitur
✅ Input fungsi tujuan (Maksimasi / Minimasi)
✅ Input fungsi kendala dinamis (dengan tanda ≤, ≥, =)
✅ Kendala non-negatif otomatis (X₁ ≥ 0, X₂ ≥ 0)
✅ Visualisasi grafik feasible region
✅ Tabel semua titik ekstrim dengan nilai Z
✅ Solusi optimal ditandai bintang ★
✅ 4 contoh kasus siap pakai dari materi kuliah:
Wyndor Glass Co.
PT Sayang Anak (Boneka & Kereta Api)
Petani (Tembakau & Kedelai)
PT Auto Indah (Promosi TV)
✅ Deteksi kasus tidak fisibel
🛠️ Instalasi

1. Pastikan Python sudah terinstall

Cek di terminal / cmd:

bash
python --version

Butuh Python 3.9 atau lebih baru.

2. Install semua library yang dibutuhkan

Buka terminal di folder ini, lalu jalankan:

bash
pip install -r requirements.txt
🚀 Cara Menjalankan

Di terminal / cmd, dari folder project ini, jalankan:

bash
streamlit run app.py

Browser akan otomatis terbuka di alamat http://localhost:8501

Untuk menghentikan: tekan Ctrl + C di terminal.

📖 Cara Menggunakan
Pilih contoh kasus di sidebar (opsional), atau input manual
Pilih jenis optimasi: Maksimasi atau Minimasi
Isi koefisien fungsi tujuan (c₁ dan c₂)
Atur jumlah kendala dan isi koefisiennya
Klik tombol 🚀 HITUNG SOLUSI OPTIMAL
Lihat hasilnya: grafik, tabel titik ekstrim, dan solusi optimal
📁 Struktur Folder
simulasi-riset-operasional/
├── app.py # Kode utama program
├── requirements.txt # Daftar library yang dibutuhkan
├── README.md # Dokumentasi ini
└── contoh-kasus/ # Folder untuk file contoh kasus (opsional)
🧮 Metode yang Digunakan

Metode Grafis menyelesaikan program linier dengan langkah:

Menggambar garis dari setiap fungsi kendala pada bidang koordinat X₁-X₂
Menentukan daerah fisibel (feasible region) yang memenuhi semua kendala
Mencari titik-titik potong antar garis kendala (titik ekstrim)
Menghitung nilai Z pada setiap titik ekstrim
Titik dengan nilai Z terbaik = solusi optimal
👨‍💻 Dibuat untuk

Tugas Mata Kuliah Riset Operasional Program Studi Teknik Informatika Universitas Komputer Indonesia
