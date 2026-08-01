# 📘 KASUS 1: WYNDOR GLASS CO.

## 🏭 Cerita Masalahnya

Perusahaan **Wyndor Glass** adalah perusahaan yang bikin kaca berkualitas tinggi (jendela & pintu). Mereka punya **3 departemen**:

- **Departemen 1**: Bikin rangka aluminium
- **Departemen 2**: Bikin rangka kayu
- **Departemen 3**: Bikin kaca & merakit produk

Karena pendapatan turun, mereka mau bikin **2 produk baru**:

- **Produk 1**: Pintu kaca dengan rangka aluminium
- **Produk 2**: Jendela rangka kayu

**PERTANYAAN:** Berapa batch setiap produk harus dibuat per minggu supaya **keuntungan maksimum**?

---

## 📊 Data Masalah

| Departemen       | Waktu Produk 1 (jam) | Waktu Produk 2 (jam) | Jam Tersedia/Minggu |
| ---------------- | :------------------: | :------------------: | :-----------------: |
| Dept. 1          |          1           |          0           |          4          |
| Dept. 2          |          0           |          2           |         12          |
| Dept. 3          |          3           |          2           |         18          |
| **Untung/batch** |      **$3.000**      |      **$5.000**      |                     |

---

## 🔢 Langkah 1: Tentukan Variabel Keputusan

Yang mau kita cari nilainya:

- **X₁** = jumlah batch Produk 1 per minggu
- **X₂** = jumlah batch Produk 2 per minggu

---

## 🎯 Langkah 2: Fungsi Tujuan

Kita mau **MEMAKSIMUMKAN keuntungan total**:

```
Maksimasi Z = 3X₁ + 5X₂
```

Artinya:

- Setiap batch Produk 1 = untung $3.000 (dibaca sebagai "3" ribu)
- Setiap batch Produk 2 = untung $5.000 (dibaca sebagai "5" ribu)
- **Z** = total keuntungan (dalam ribuan dolar)

---

## ⚖️ Langkah 3: Fungsi Kendala

**Kendala 1** — Kapasitas Dept. 1 max 4 jam/minggu:

```
1X₁ + 0X₂ ≤ 4   →  X₁ ≤ 4
```

**Kendala 2** — Kapasitas Dept. 2 max 12 jam/minggu:

```
0X₁ + 2X₂ ≤ 12  →  2X₂ ≤ 12
```

**Kendala 3** — Kapasitas Dept. 3 max 18 jam/minggu:

```
3X₁ + 2X₂ ≤ 18
```

**Kendala Non-Negatif** (otomatis di program):

```
X₁ ≥ 0
X₂ ≥ 0
```

---

## 💻 Cara Input di Program

Buka aplikasi → di sidebar isi:

### Fungsi Tujuan:

| Field          | Isi           |
| -------------- | ------------- |
| Jenis Optimasi | **Maksimasi** |
| Koef. X₁       | **3**         |
| Koef. X₂       | **5**         |

### Jumlah Kendala: **3**

### Kendala 1:

| Field       | Isi |
| ----------- | --- |
| Koef X₁     | 1   |
| Koef X₂     | 0   |
| Operator    | ≤   |
| Nilai (RHS) | 4   |

### Kendala 2:

| Field       | Isi |
| ----------- | --- |
| Koef X₁     | 0   |
| Koef X₂     | 2   |
| Operator    | ≤   |
| Nilai (RHS) | 12  |

### Kendala 3:

| Field       | Isi |
| ----------- | --- |
| Koef X₁     | 3   |
| Koef X₂     | 2   |
| Operator    | ≤   |
| Nilai (RHS) | 18  |

Klik **🚀 HITUNG SOLUSI OPTIMAL**

---

## ✅ Jawaban yang Diharapkan

**Solusi Optimal:**

- **X₁ = 2** batch Produk 1 per minggu
- **X₂ = 6** batch Produk 2 per minggu
- **Z = $36** (yaitu $36.000/minggu)

**Kesimpulan:** Wyndor Glass harus produksi 2 batch pintu kaca & 6 batch jendela per minggu untuk untung maksimum $36.000/minggu.
