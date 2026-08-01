# 📙 KASUS 3: PETANI (TEMBAKAU & KEDELAI)

## 🌾 Cerita Masalahnya

Seorang **petani** punya lahan yang mau ditanami **tembakau** dan **kedelai**.

### Data:

- Total lahan yang tersedia: **maksimal 150 hektar**
- Tembakau butuh: **100 jam kerja/hektar**
- Kedelai butuh: **200 jam kerja/hektar**
- Total jam kerja tersedia sampai panen: **maksimal 16.000 jam**
- Lahan tembakau **minimal 20 hektar** (harus ditanami)
- Keuntungan tembakau: **Rp 75.000/hektar**
- Keuntungan kedelai: **Rp 25.000/hektar**

**PERTANYAAN:** Berapa hektar lahan yang harus ditanami tembakau & kedelai supaya **keuntungan maksimum**?

---

## 🔢 Langkah 1: Variabel Keputusan

- **X₁** = luas lahan tembakau (hektar)
- **X₂** = luas lahan kedelai (hektar)

---

## 🎯 Langkah 2: Fungsi Tujuan

**MEMAKSIMUMKAN keuntungan:**

```
Maksimasi Z = 75.000X₁ + 25.000X₂
```

---

## ⚖️ Langkah 3: Fungsi Kendala

**Kendala 1** — Total lahan max 150 hektar:

```
X₁ + X₂ ≤ 150
```

**Kendala 2** — Total jam kerja max 16.000 jam:

```
100X₁ + 200X₂ ≤ 16.000
```

**Kendala 3** — Tembakau minimal 20 hektar:

```
X₁ ≥ 20
```

**Kendala Non-Negatif:**

```
X₁ ≥ 0, X₂ ≥ 0
```

---

## 💻 Cara Input di Program

### Fungsi Tujuan:

| Field          | Isi           |
| -------------- | ------------- |
| Jenis Optimasi | **Maksimasi** |
| Koef. X₁       | **75000**     |
| Koef. X₂       | **25000**     |

### Jumlah Kendala: **3**

### Kendala 1 (total lahan):

| Koef X₁ | Koef X₂ | Operator | RHS |
| :-----: | :-----: | :------: | :-: |
|    1    |    1    |    ≤     | 150 |

### Kendala 2 (jam kerja):

| Koef X₁ | Koef X₂ | Operator |  RHS  |
| :-----: | :-----: | :------: | :---: |
|   100   |   200   |    ≤     | 16000 |

### Kendala 3 (min tembakau):

| Koef X₁ | Koef X₂ | Operator | RHS |
| :-----: | :-----: | :------: | :-: |
|    1    |    0    |  **≥**   | 20  |

⚠️ **Perhatian:** Operator kendala 3 pake **≥** (bukan ≤), karena minimal!

Klik **🚀 HITUNG SOLUSI OPTIMAL**

---

## ✅ Jawaban yang Diharapkan

**Solusi Optimal:**

- **X₁ = 150** hektar tembakau (semua lahan buat tembakau)
- **X₂ = 0** hektar kedelai (tidak tanam kedelai)
- **Z = 11.250.000** (yaitu **Rp 11.250.000**)

### 🧮 Hitungan:

```
Z = 75.000(150) + 25.000(0)
Z = 11.250.000
```

### 🔍 Verifikasi Kendala:

| Kendala                | Cek                |
| ---------------------- | ------------------ |
| X₁ + X₂ ≤ 150          | 150 + 0 = 150 ✅   |
| 100X₁ + 200X₂ ≤ 16.000 | 15.000 ≤ 16.000 ✅ |
| X₁ ≥ 20                | 150 ≥ 20 ✅        |

### 🎓 Kesimpulan:

Petani harus menanam **150 hektar tembakau** (semua lahan) dan **tidak menanam kedelai** untuk untung maksimum **Rp 11.250.000**.

---

## 🤔 Kenapa Semua Lahan untuk Tembakau?

Karena **tembakau jauh lebih menguntungkan per hektar** dibanding kedelai:

- Tembakau: Rp 75.000/hektar
- Kedelai: Rp 25.000/hektar (3x lebih kecil)

**Cek jam kerja:**

- 150 hektar tembakau × 100 jam/hektar = **15.000 jam**
- Batas maksimal jam kerja = 16.000 jam
- Masih ada sisa 1.000 jam kerja **tapi lahan udah habis**

Jadi meskipun jam kerja masih tersedia, kita gak bisa nambah kedelai karena kendala lahan sudah pas 150 hektar.

**Kesimpulan matematis:** Karena tembakau lebih untung DAN kendala lahan lebih ketat dari kendala jam kerja, optimal-nya semua lahan dipake tembakau.
