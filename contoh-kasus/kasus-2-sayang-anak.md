# 📗 KASUS 2: PT SAYANG ANAK

## 🧸 Cerita Masalahnya

**PT Sayang Anak** memproduksi 2 jenis mainan dari kayu:

- **Boneka Kayu**
- **Kereta Api Kayu**

Untuk bikin mainan, perlu 2 kelompok tenaga kerja:
- **Tukang Kayu** (pengerjaan kayu)
- **Tukang Poles** (pemolesan)

**PERTANYAAN:** Berapa lusin setiap mainan harus dibuat per minggu supaya **keuntungan maksimum**?

---

## 📊 Data Masalah

| Item | Boneka Kayu | Kereta Api Kayu |
|------|:-:|:-:|
| Harga jual | Rp 27.000/lusin | Rp 21.000/lusin |
| Biaya material | Rp 10.000/lusin | Rp 9.000/lusin |
| Biaya tenaga kerja | Rp 14.000/lusin | Rp 10.000/lusin |
| Waktu pemolesan | 2 jam | 1 jam |
| Waktu pengerjaan kayu | 1 jam | 1 jam |

### Batasan lain:
- Jam pemolesan tersedia: **100 jam/minggu**
- Jam pengerjaan kayu tersedia: **80 jam/minggu**
- Boneka: max **40 lusin/minggu** (permintaan pasar terbatas)
- Kereta api: permintaan tidak terbatas

---

## 💰 Hitung Keuntungan per Lusin

**Boneka:**
```
Untung = Harga jual - Biaya material - Biaya tenaga kerja
       = 27.000 - 10.000 - 14.000
       = Rp 3.000/lusin
```

**Kereta Api:**
```
Untung = 21.000 - 9.000 - 10.000
       = Rp 2.000/lusin
```

---

## 🔢 Langkah 1: Variabel Keputusan

- **X₁** = jumlah lusin boneka kayu per minggu
- **X₂** = jumlah lusin kereta api kayu per minggu

---

## 🎯 Langkah 2: Fungsi Tujuan

**MEMAKSIMUMKAN keuntungan** (dalam ribuan rupiah):

```
Maksimasi Z = 3X₁ + 2X₂
```

---

## ⚖️ Langkah 3: Fungsi Kendala

**Kendala 1** — Jam pemolesan max 100 jam/minggu:
```
2X₁ + 1X₂ ≤ 100
```
(Boneka butuh 2 jam poles, Kereta butuh 1 jam poles)

**Kendala 2** — Jam pengerjaan kayu max 80 jam/minggu:
```
1X₁ + 1X₂ ≤ 80
```

**Kendala 3** — Permintaan boneka max 40 lusin/minggu:
```
1X₁ + 0X₂ ≤ 40  →  X₁ ≤ 40
```

**Kendala Non-Negatif:**
```
X₁ ≥ 0, X₂ ≥ 0
```

---

## 💻 Cara Input di Program

### Fungsi Tujuan:
| Field | Isi |
|-------|-----|
| Jenis Optimasi | **Maksimasi** |
| Koef. X₁ | **3** |
| Koef. X₂ | **2** |

### Jumlah Kendala: **3**

### Kendala 1 (jam pemolesan):
| Koef X₁ | Koef X₂ | Operator | RHS |
|:-:|:-:|:-:|:-:|
| 2 | 1 | ≤ | 100 |

### Kendala 2 (jam pengerjaan kayu):
| Koef X₁ | Koef X₂ | Operator | RHS |
|:-:|:-:|:-:|:-:|
| 1 | 1 | ≤ | 80 |

### Kendala 3 (batas boneka):
| Koef X₁ | Koef X₂ | Operator | RHS |
|:-:|:-:|:-:|:-:|
| 1 | 0 | ≤ | 40 |

Klik **🚀 HITUNG SOLUSI OPTIMAL**

---

## ✅ Jawaban yang Diharapkan

**Solusi Optimal:**
- **X₁ = 20** lusin boneka per minggu
- **X₂ = 60** lusin kereta api per minggu
- **Z = 180** (yaitu Rp 180.000/minggu)

**Kesimpulan:** PT Sayang Anak harus produksi 20 lusin boneka & 60 lusin kereta api per minggu untuk untung maksimum Rp 180.000/minggu.
