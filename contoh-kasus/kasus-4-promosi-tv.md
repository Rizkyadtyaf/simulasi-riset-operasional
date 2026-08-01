# 📕 KASUS 4: PT AUTO INDAH (PROMOSI TV)

## 📺 Cerita Masalahnya

**PT Auto Indah** memproduksi 2 jenis mobil: **sedan** dan **truk**. Untuk meraih konsumen berpenghasilan tinggi, mereka memutuskan promosi di **2 acara TV**:

- **Acara Hiburan**
- **Acara Olah Raga**

### Data Pemirsa & Biaya:

| Item           |  Acara Hiburan   | Acara Olah Raga  |
| -------------- | :--------------: | :--------------: |
| Pemirsa Wanita |     10 juta      |      6 juta      |
| Pemirsa Pria   |      5 juta      |     18 juta      |
| Biaya          | Rp 10 juta/menit | Rp 30 juta/menit |

### Target Perusahaan:

- Sedikitnya **40 juta pemirsa wanita** harus lihat
- Sedikitnya **35 juta pemirsa pria** harus lihat

**PERTANYAAN:** Berapa menit promosi di masing-masing acara supaya **biaya minimum** tapi target pemirsa tercapai?

---

## 🔢 Langkah 1: Variabel Keputusan

- **X₁** = menit promosi di acara hiburan
- **X₂** = menit promosi di acara olah raga

---

## 🎯 Langkah 2: Fungsi Tujuan

⚠️ **Ini kasus MINIMASI** (bukan maksimasi)! Karena kita mau **biaya sekecil mungkin**.

```
Minimasi Z = 10X₁ + 30X₂
```

(dalam satuan juta rupiah)

---

## ⚖️ Langkah 3: Fungsi Kendala

**Kendala 1** — Minimal 40 juta pemirsa wanita:

```
10X₁ + 6X₂ ≥ 40
```

**Kendala 2** — Minimal 35 juta pemirsa pria:

```
5X₁ + 18X₂ ≥ 35
```

**Kendala Non-Negatif:**

```
X₁ ≥ 0, X₂ ≥ 0
```

---

## 💻 Cara Input di Program

### Fungsi Tujuan:

| Field          | Isi             |
| -------------- | --------------- |
| Jenis Optimasi | **Minimasi** ⚠️ |
| Koef. X₁       | **10**          |
| Koef. X₂       | **30**          |

### Jumlah Kendala: **2**

### Kendala 1 (pemirsa wanita):

| Koef X₁ | Koef X₂ | Operator | RHS |
| :-----: | :-----: | :------: | :-: |
|   10    |    6    |  **≥**   | 40  |

### Kendala 2 (pemirsa pria):

| Koef X₁ | Koef X₂ | Operator | RHS |
| :-----: | :-----: | :------: | :-: |
|    5    |   18    |  **≥**   | 35  |

⚠️ **Perhatian:** Kedua operator pake **≥** (minimal), bukan ≤!

Klik **🚀 HITUNG SOLUSI OPTIMAL**

---

## ✅ Jawaban yang Diharapkan

**Solusi Optimal:**

- **X₁ = 3.40** menit di acara hiburan
- **X₂ = 1.00** menit di acara olah raga
- **Z = 64.00** (yaitu **Rp 64 juta**)

### 🧮 Hitungan:

```
Z = 10(3.40) + 30(1.00)
Z = 34 + 30
Z = 64
```

### 🔍 Verifikasi Kendala:

| Kendala                          | Cek                              |
| -------------------------------- | -------------------------------- |
| 10X₁ + 6X₂ ≥ 40 (pemirsa wanita) | 10(3.4) + 6(1) = 40 ✅ pas batas |
| 5X₁ + 18X₂ ≥ 35 (pemirsa pria)   | 5(3.4) + 18(1) = 35 ✅ pas batas |

### 🎓 Kesimpulan:

PT Auto Indah harus promosi:

- **3,4 menit di acara hiburan**
- **1 menit di acara olah raga**

**Total biaya minimum: Rp 64 juta**

Dengan begitu, target pemirsa tercapai pas di batas minimum:

- Pemirsa wanita: **40 juta** (sesuai target)
- Pemirsa pria: **35 juta** (sesuai target)

---

## 💡 Beda Maksimasi vs Minimasi

| Aspek            | Maksimasi                   | Minimasi                   |
| ---------------- | --------------------------- | -------------------------- |
| Tujuan           | Cari Z **paling besar**     | Cari Z **paling kecil**    |
| Biasanya untuk   | Keuntungan, penjualan       | Biaya, waktu, jarak        |
| Operator kendala | Biasanya ≤ (batas atas)     | Biasanya ≥ (batas bawah)   |
| Titik optimal    | Di pojok terjauh dari (0,0) | Di pojok terdekat ke (0,0) |

---

## 🤔 Kenapa Solusinya Pas di Batas?

Karena kita mau **biaya minimum**, tapi ada target pemirsa yang **harus dipenuhi**. Optimalnya adalah:

- **Cukup untuk mencapai target** (biar gak boros)
- **Gak lebih dari yang dibutuhkan** (biar hemat)

Jadi solusi optimal biasanya berada **pas di titik pertemuan** dua kendala (batas minimum kedua target tercapai bersamaan).
