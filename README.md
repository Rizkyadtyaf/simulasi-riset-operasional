# 📊 Simulasi Optimasi Program Linier - Metode Grafis

Program simulasi untuk menyelesaikan masalah **Program Linier 2 variabel** dengan **Metode Grafis (Geometris)**.

> **Mata Kuliah:** Riset Operasional  
> **Materi:** Pertemuan 2 - Program Linier dan Metode Grafis  
> **Program Studi:** Teknik Informatika, Universitas Komputer Indonesia

---

## 🎯 Fitur

- ✅ Input fungsi tujuan (Maksimasi / Minimasi)
- ✅ Input fungsi kendala dinamis (dengan tanda ≤, ≥, =)
- ✅ Kendala non-negatif otomatis (X₁ ≥ 0, X₂ ≥ 0)
- ✅ Input nama kasus custom
- ✅ Visualisasi grafik feasible region
- ✅ Tabel semua titik ekstrim dengan nilai Z
- ✅ Solusi optimal ditandai bintang ★
- ✅ Validasi otomatis untuk input yang tidak valid
- ✅ Deteksi kasus tidak fisibel
- ✅ 4 contoh kasus siap pakai dari materi kuliah:
  - Wyndor Glass Co.
  - PT Sayang Anak (Boneka & Kereta Api)
  - Petani (Tembakau & Kedelai)
  - PT Auto Indah (Promosi TV)

---

## 🛠️ Instalasi

### 1. Pastikan Python sudah terinstall

Cek di terminal / cmd:

```bash
python --version
```

Butuh Python 3.9 atau lebih baru.

### 2. Install semua library yang dibutuhkan

Buka terminal di folder ini, lalu jalankan:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cara Menjalankan

Di terminal / cmd, dari folder project ini, jalankan:

```bash
streamlit run app.py
```

Browser akan otomatis terbuka di alamat `http://localhost:8501`

Untuk menghentikan: tekan **Ctrl + C** di terminal.

---

## 📖 Cara Menggunakan

### Mode 1: Pakai Contoh Kasus dari Materi

1. Di sidebar, pilih dropdown **"Contoh Kasus"**
2. Pilih salah satu (Wyndor Glass / PT Sayang Anak / Petani / PT Auto Indah)
3. Semua field auto-terisi sesuai kasus
4. Klik **🚀 HITUNG SOLUSI OPTIMAL**

### Mode 2: Bikin Kasus Sendiri (Custom)

1. Di dropdown "Contoh Kasus", biarkan di **"-- Pilih contoh kasus --"**
2. Kolom **"Nama Kasus"** akan muncul otomatis — isi nama kasusmu (contoh: "Kantin Bu Sinta")
3. Isi manual: jenis optimasi, koefisien fungsi tujuan, dan kendala-kendala
4. Klik **🚀 HITUNG SOLUSI OPTIMAL**

---

## 📁 Struktur Folder

```
simulasi-riset-operasional/
├── app.py              # Kode utama program
├── requirements.txt    # Daftar library yang dibutuhkan
├── README.md           # Dokumentasi ini
└── contoh-kasus/       # Penjelasan lengkap contoh kasus
    ├── README-contoh-kasus.md
    ├── kasus-1-wyndor-glass.md
    ├── kasus-2-sayang-anak.md
    ├── kasus-3-petani.md
    └── kasus-4-promosi-tv.md
```

---

## 🧮 Metode yang Digunakan

**Metode Grafis** menyelesaikan program linier dengan langkah:

1. Menggambar garis dari setiap fungsi kendala pada bidang koordinat X₁-X₂
2. Menentukan daerah fisibel (feasible region) yang memenuhi semua kendala
3. Mencari titik-titik potong antar garis kendala (titik ekstrim)
4. Menghitung nilai Z pada setiap titik ekstrim
5. Titik dengan nilai Z terbaik = solusi optimal

---

## ✅ Hasil Uji Contoh Kasus

Semua contoh kasus sudah diverifikasi sesuai materi:

| Kasus                       | X₁  | X₂  | Z Optimal  |
| --------------------------- | :-: | :-: | :--------: |
| Wyndor Glass Co.            |  2  |  6  |     36     |
| PT Sayang Anak              | 20  | 60  |    180     |
| Petani (Tembakau & Kedelai) | 150 |  0  | 11.250.000 |
| PT Auto Indah (Promosi TV)  | 3.4 |  1  |     64     |

---

## 🧰 Tech Stack

- **Python 3.9+**
- **Streamlit** — Web framework
- **NumPy** — Perhitungan numerik
- **Matplotlib** — Visualisasi grafik
- **Pandas** — Tabel data
- **SciPy** — Library ilmiah

---

## 👨‍💻 Dibuat untuk

Tugas Mata Kuliah **Riset Operasional**  
Program Studi Teknik Informatika  
Universitas Komputer Indonesia <br>
**Nama : Lidan Wisnu Saputra**
