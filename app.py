"""
SIMULASI OPTIMASI PROGRAM LINIER - METODE GRAFIS
Mata Kuliah: Riset Operasional
Universitas Komputer Indonesia
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from itertools import combinations

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title="Simulasi Program Linier",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    section[data-testid="stSidebar"][aria-expanded="true"] {
        min-width: 380px !important;
        max-width: 380px !important;
    }
    div[data-testid="stNumberInput"] input {
        text-align: center;
        font-weight: 600;
    }
    h1 { color: #1e3c72; }
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #3b82f6;
    }
    .stAlert { border-radius: 10px; }
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# CONTOH KASUS
# ============================================================
CONTOH_KASUS = {
    "-- Pilih contoh kasus --": None,
    "Wyndor Glass Co.": {
        'jenis': 'Maksimasi', 'c1': 3, 'c2': 5,
        'kendala': [
            {'a1': 1, 'a2': 0, 'op': '<=', 'b': 4},
            {'a1': 0, 'a2': 2, 'op': '<=', 'b': 12},
            {'a1': 3, 'a2': 2, 'op': '<=', 'b': 18},
        ]
    },
    "PT Sayang Anak": {
        'jenis': 'Maksimasi', 'c1': 3, 'c2': 2,
        'kendala': [
            {'a1': 2, 'a2': 1, 'op': '<=', 'b': 100},
            {'a1': 1, 'a2': 1, 'op': '<=', 'b': 80},
            {'a1': 1, 'a2': 0, 'op': '<=', 'b': 40},
        ]
    },
    "Petani (Tembakau & Kedelai)": {
        'jenis': 'Maksimasi', 'c1': 75000, 'c2': 25000,
        'kendala': [
            {'a1': 1, 'a2': 1, 'op': '<=', 'b': 150},
            {'a1': 100, 'a2': 200, 'op': '<=', 'b': 16000},
            {'a1': 1, 'a2': 0, 'op': '>=', 'b': 20},
        ]
    },
    "PT Auto Indah (Promosi TV)": {
        'jenis': 'Minimasi', 'c1': 10, 'c2': 30,
        'kendala': [
            {'a1': 10, 'a2': 6, 'op': '>=', 'b': 40},
            {'a1': 5, 'a2': 18, 'op': '>=', 'b': 35},
        ]
    },
}


# ============================================================
# INIT SESSION STATE (jalan sekali pas app pertama load)
# ============================================================
def init_session_state():
    """Set default values ke session_state kalau belum ada."""
    defaults = {
        'jenis': 'Maksimasi',
        'c1': 3.0,
        'c2': 5.0,
        'jumlah_kendala': 3,
        'nama_kasus_custom': '',
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val
    
    # Default 3 kendala
    default_kendala = [
        {'a1': 1.0, 'a2': 0.0, 'op': '≤', 'b': 4.0},
        {'a1': 0.0, 'a2': 2.0, 'op': '≤', 'b': 12.0},
        {'a1': 3.0, 'a2': 2.0, 'op': '≤', 'b': 18.0},
    ]
    for i, k in enumerate(default_kendala):
        if f'a1_{i}' not in st.session_state:
            st.session_state[f'a1_{i}'] = k['a1']
        if f'a2_{i}' not in st.session_state:
            st.session_state[f'a2_{i}'] = k['a2']
        if f'op_{i}' not in st.session_state:
            st.session_state[f'op_{i}'] = k['op']
        if f'b_{i}' not in st.session_state:
            st.session_state[f'b_{i}'] = k['b']


# ============================================================
# CALLBACK: Reset semua field saat dropdown contoh kasus berubah
# ============================================================
def load_contoh_kasus():
    """Callback jalan SEBELUM widget di-render."""
    pilihan = st.session_state.get('pilihan_contoh', '-- Pilih contoh kasus --')
    
    if pilihan == '-- Pilih contoh kasus --':
        return
    
    data = CONTOH_KASUS[pilihan]
    if data is None:
        return
    
    st.session_state['jenis'] = data['jenis']
    st.session_state['c1'] = float(data['c1'])
    st.session_state['c2'] = float(data['c2'])
    st.session_state['jumlah_kendala'] = len(data['kendala'])
    
    op_map_reverse = {'<=': '≤', '>=': '≥', '=': '='}
    for i, k in enumerate(data['kendala']):
        st.session_state[f'a1_{i}'] = float(k['a1'])
        st.session_state[f'a2_{i}'] = float(k['a2'])
        st.session_state[f'b_{i}'] = float(k['b'])
        st.session_state[f'op_{i}'] = op_map_reverse[k['op']]


# ============================================================
# VALIDASI KENDALA
# ============================================================
def validasi_kendala(kendala_input):
    kendala_invalid = []
    for i, k in enumerate(kendala_input):
        if abs(k['a1']) < 1e-10 and abs(k['a2']) < 1e-10:
            kendala_invalid.append(i + 1)
    return kendala_invalid


# ============================================================
# SOLVER - METODE GRAFIS
# ============================================================
def cari_titik_potong(k1, k2):
    a1, b1, c1 = k1['a1'], k1['a2'], k1['b']
    a2, b2, c2 = k2['a1'], k2['a2'], k2['b']
    det = a1 * b2 - a2 * b1
    if abs(det) < 1e-10:
        return None
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return (x, y)


def cek_fisibel(titik, kendala_list, eps=1e-6):
    x, y = titik
    for k in kendala_list:
        nilai = k['a1'] * x + k['a2'] * y
        if k['op'] == '<=' and nilai > k['b'] + eps:
            return False
        if k['op'] == '>=' and nilai < k['b'] - eps:
            return False
        if k['op'] == '=' and abs(nilai - k['b']) > eps:
            return False
    return True


def selesaikan_program_linier(jenis_optimasi, c1, c2, kendala_input):
    semua_kendala = kendala_input + [
        {'a1': 1, 'a2': 0, 'op': '>=', 'b': 0},
        {'a1': 0, 'a2': 1, 'op': '>=', 'b': 0}
    ]

    titik_potong = []
    for k1, k2 in combinations(semua_kendala, 2):
        p = cari_titik_potong(k1, k2)
        if p is not None:
            titik_potong.append(p)

    titik_fisibel = [p for p in titik_potong if cek_fisibel(p, semua_kendala)]

    titik_unik = []
    for p in titik_fisibel:
        duplikat = False
        for q in titik_unik:
            if abs(p[0] - q[0]) < 1e-6 and abs(p[1] - q[1]) < 1e-6:
                duplikat = True
                break
        if not duplikat:
            titik_unik.append(p)

    if len(titik_unik) == 0:
        return {'status': 'tidak_fisibel', 'titik_ekstrim': [], 'optimal': None}

    hasil = []
    for x, y in titik_unik:
        z = c1 * x + c2 * y
        hasil.append({'x1': x, 'x2': y, 'z': z})

    if jenis_optimasi == 'Maksimasi':
        optimal = max(hasil, key=lambda h: h['z'])
    else:
        optimal = min(hasil, key=lambda h: h['z'])

    return {
        'status': 'optimal',
        'titik_ekstrim': hasil,
        'optimal': optimal,
        'semua_kendala': semua_kendala
    }


# ============================================================
# VISUALISASI - GRAFIK
# ============================================================
def gambar_grafik(hasil, c1, c2, kendala_input, nama_kasus=""):
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor('#ffffff')

    if hasil['titik_ekstrim']:
        max_x = max([t['x1'] for t in hasil['titik_ekstrim']] + [10]) * 1.3
        max_y = max([t['x2'] for t in hasil['titik_ekstrim']] + [10]) * 1.3
    else:
        max_x, max_y = 20, 20

    x_range = np.linspace(0, max_x, 500)
    warna = ['#e53e3e', '#3182ce', '#805ad5', '#d69e2e', '#319795', '#dd6b20', '#9f7aea']

    X, Y = np.meshgrid(np.linspace(0, max_x, 300), np.linspace(0, max_y, 300))
    fisibel = np.ones_like(X, dtype=bool)
    for k in kendala_input + [{'a1': 1, 'a2': 0, 'op': '>=', 'b': 0},
                                {'a1': 0, 'a2': 1, 'op': '>=', 'b': 0}]:
        nilai = k['a1'] * X + k['a2'] * Y
        if k['op'] == '<=':
            fisibel &= (nilai <= k['b'] + 1e-6)
        elif k['op'] == '>=':
            fisibel &= (nilai >= k['b'] - 1e-6)
        else:
            fisibel &= (np.abs(nilai - k['b']) < 1e-6)

    ax.contourf(X, Y, fisibel.astype(int), levels=[0.5, 1.5],
                colors=['#48bb78'], alpha=0.25)

    for i, k in enumerate(kendala_input):
        label = f"{k['a1']:g}X₁ + {k['a2']:g}X₂ {k['op']} {k['b']:g}"
        c = warna[i % len(warna)]
        
        if abs(k['a1']) < 1e-10 and abs(k['a2']) < 1e-10:
            continue
        
        if abs(k['a2']) > 1e-10:
            y_vals = (k['b'] - k['a1'] * x_range) / k['a2']
            ax.plot(x_range, y_vals, color=c, linewidth=2.5, label=label)
        elif abs(k['a1']) > 1e-10:
            x_vert = k['b'] / k['a1']
            ax.axvline(x=x_vert, color=c, linewidth=2.5, label=label)

    for i, t in enumerate(hasil['titik_ekstrim']):
        is_optimal = (t == hasil['optimal'])
        color = '#e53e3e' if is_optimal else '#2a5298'
        size = 300 if is_optimal else 120
        marker = '*' if is_optimal else 'o'
        ax.scatter(t['x1'], t['x2'], s=size, c=color, marker=marker,
                   zorder=5, edgecolors='white', linewidths=2)
        label_titik = f"({t['x1']:.1f}, {t['x2']:.1f})"
        if is_optimal:
            label_titik += " ★"
        ax.annotate(label_titik, (t['x1'], t['x2']),
                    textcoords="offset points", xytext=(12, 12),
                    fontsize=11, fontweight='bold' if is_optimal else 'normal',
                    color=color,
                    bbox=dict(boxstyle='round,pad=0.3',
                              facecolor='white', edgecolor=color, alpha=0.8))

    ax.set_xlim(0, max_x)
    ax.set_ylim(0, max_y)
    ax.set_xlabel('X₁', fontsize=13, fontweight='bold')
    ax.set_ylabel('X₂', fontsize=13, fontweight='bold')
    
    if nama_kasus:
        judul = f'{nama_kasus}\nGrafik Feasible Region  |  Z = {c1:g}X₁ + {c2:g}X₂'
    else:
        judul = f'Grafik Feasible Region  |  Z = {c1:g}X₁ + {c2:g}X₂'
    ax.set_title(judul, fontsize=13, fontweight='bold', pad=15)
    
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax.axhline(y=0, color='black', linewidth=0.8)
    ax.axvline(x=0, color='black', linewidth=0.8)
    ax.set_facecolor('#fafbfc')

    plt.tight_layout()
    return fig


# ============================================================
# UI STREAMLIT
# ============================================================
def main():
    # Init session state pertama kali
    init_session_state()
    
    col_h1, col_h2 = st.columns([1, 5])

    with col_h2:
        st.markdown("# Simulasi Optimasi Program Linier")
        st.caption("**Metode Grafis (Geometris)** — Mata Kuliah Riset Operasional")
    st.markdown("---")

    with st.sidebar:
        st.markdown("## Input Masalah")
        
        st.markdown("#### Contoh Kasus")
        # Widget pakai KEY doang, tanpa value/index (biar gak warning)
        pilihan_contoh = st.selectbox(
            "Pilih contoh:",
            list(CONTOH_KASUS.keys()),
            key='pilihan_contoh',
            on_change=load_contoh_kasus,
            label_visibility="collapsed"
        )
        
        nama_kasus = ""
        if pilihan_contoh == "-- Pilih contoh kasus --":
            nama_kasus = st.text_input(
                "Nama Kasus Kamu:",
                placeholder="Contoh: Kantin Lidan",
                help="Isi nama kasus buatanmu di sini",
                key='nama_kasus_custom'
            )
        else:
            nama_kasus = pilihan_contoh

        st.markdown("---")

        # Fungsi Tujuan — cuma pake key, tanpa value/index
        st.markdown("#### Fungsi Tujuan")
        
        jenis = st.radio(
            "Jenis Optimasi:",
            ["Maksimasi", "Minimasi"],
            horizontal=True,
            key='jenis'
        )

        col1, col2 = st.columns(2)
        with col1:
            c1 = st.number_input(
                "Koef. X₁", 
                step=1.0, 
                format="%.2f",
                key='c1'
            )
        with col2:
            c2 = st.number_input(
                "Koef. X₂", 
                step=1.0, 
                format="%.2f",
                key='c2'
            )

        st.info(f"**Z = {c1:g}X₁ + {c2:g}X₂**")

        st.markdown("---")

        # Fungsi Kendala
        st.markdown("#### Fungsi Kendala")
        jumlah_kendala = st.number_input(
            "Jumlah Kendala:",
            min_value=1, max_value=8,
            step=1,
            key='jumlah_kendala'
        )

        # Pastikan session_state ada untuk semua kendala yg diperlukan
        for i in range(jumlah_kendala):
            if f'a1_{i}' not in st.session_state:
                st.session_state[f'a1_{i}'] = 1.0
            if f'a2_{i}' not in st.session_state:
                st.session_state[f'a2_{i}'] = 1.0
            if f'op_{i}' not in st.session_state:
                st.session_state[f'op_{i}'] = '≤'
            if f'b_{i}' not in st.session_state:
                st.session_state[f'b_{i}'] = 10.0

        kendala_input = []
        
        for i in range(jumlah_kendala):
            with st.container():
                st.markdown(f"**Kendala {i+1}**")
                
                col_a, col_b = st.columns(2)
                with col_a:
                    a1 = st.number_input(
                        f"Koef X₁",
                        step=1.0,
                        key=f"a1_{i}",
                        format="%.2f"
                    )
                with col_b:
                    a2 = st.number_input(
                        f"Koef X₂",
                        step=1.0,
                        key=f"a2_{i}",
                        format="%.2f"
                    )
                
                col_c, col_d = st.columns([1, 1])
                with col_c:
                    op_display = st.selectbox(
                        "Operator",
                        ["≤", "≥", "="],
                        key=f"op_{i}"
                    )
                    op_map = {"≤": "<=", "≥": ">=", "=": "="}
                    op = op_map[op_display]
                with col_d:
                    b = st.number_input(
                        "Nilai (RHS)",
                        step=1.0,
                        key=f"b_{i}",
                        format="%.2f"
                    )
                
                if abs(a1) < 1e-10 and abs(a2) < 1e-10:
                    st.warning(f"⚠️ Kendala {i+1} tidak valid! Koef X₁ dan X₂ tidak boleh dua-duanya 0.")
                else:
                    st.caption(f"👉 {a1:g}X₁ + {a2:g}X₂ {op} {b:g}")
                st.markdown("")

            kendala_input.append({'a1': a1, 'a2': a2, 'op': op, 'b': b})

        st.markdown("---")
        st.caption("🔒 X₁ ≥ 0 dan X₂ ≥ 0 otomatis ditambahkan")

        hitung = st.button(
            "🚀 HITUNG SOLUSI OPTIMAL",
            use_container_width=True,
            type="primary"
        )

    # ========== MAIN AREA ==========
    if hitung:
        kendala_invalid = validasi_kendala(kendala_input)
        if kendala_invalid:
            st.error(f"""
            ❌ **Kendala tidak valid!**
            
            Kendala nomor **{', '.join(map(str, kendala_invalid))}** memiliki Koef X₁ = 0 dan Koef X₂ = 0 
            secara bersamaan. Ini bukan kendala yang valid.
            
            **Perbaiki di sidebar:** minimal salah satu (Koef X₁ atau Koef X₂) harus bukan 0.
            """)
            return
        
        with st.spinner("Menghitung solusi optimal..."):
            hasil = selesaikan_program_linier(jenis, c1, c2, kendala_input)

        if hasil['status'] == 'tidak_fisibel':
            st.error("❌ **Tidak ada solusi fisibel!** Kendala saling bertentangan.")
            return

        if nama_kasus:
            st.markdown(f"## 📌 Kasus: **{nama_kasus}**")
            st.markdown("---")

        st.markdown("### 📝 Formulasi Masalah")
        col_a, col_b = st.columns([1, 1])
        with col_a:
            with st.container(border=True):
                st.markdown(f"**{jenis} Z = {c1:g}X₁ + {c2:g}X₂**")
                st.markdown("**Fungsi Kendala:**")
                for k in kendala_input:
                    st.markdown(f"- {k['a1']:g}X₁ + {k['a2']:g}X₂ {k['op']} {k['b']:g}")
                st.markdown("- X₁ ≥ 0, X₂ ≥ 0")

        with col_b:
            with st.container(border=True):
                st.markdown("**Variabel Keputusan:**")
                st.markdown("- **X₁** = jumlah produksi jenis 1")
                st.markdown("- **X₂** = jumlah produksi jenis 2")
                st.markdown(f"- **Z** = total {'keuntungan' if jenis == 'Maksimasi' else 'biaya'}")

        st.markdown("---")

        st.markdown("### 📈 Grafik Feasible Region")
        fig = gambar_grafik(hasil, c1, c2, kendala_input, nama_kasus)
        st.pyplot(fig)

        st.markdown("---")

        st.markdown("### 📋 Tabel Titik-Titik Ekstrim")
        df_data = []
        for i, t in enumerate(hasil['titik_ekstrim']):
            is_opt = (t == hasil['optimal'])
            df_data.append({
                'Titik': f"{chr(65+i)}{' ⭐' if is_opt else ''}",
                'X₁': f"{t['x1']:.2f}",
                'X₂': f"{t['x2']:.2f}",
                f'Z = {c1:g}X₁ + {c2:g}X₂': f"{t['z']:.2f}",
                'Status': '✅ OPTIMAL' if is_opt else '-'
            })
        df = pd.DataFrame(df_data)
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.markdown("---")

        st.markdown(f"### ✅ Solusi Optimal ({jenis})")
        opt = hasil['optimal']
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("X₁", f"{opt['x1']:.2f}")
        with col2:
            st.metric("X₂", f"{opt['x2']:.2f}")
        with col3:
            st.metric(f"Z ({jenis})", f"{opt['z']:.2f}")

        kesimpulan_judul = f"💡 Kesimpulan {nama_kasus}:" if nama_kasus else "💡 Kesimpulan:"
        st.success(f"""
        **{kesimpulan_judul}**
        
        Untuk mencapai nilai Z yang **{'MAKSIMUM' if jenis == 'Maksimasi' else 'MINIMUM'}**, 
        variabel keputusan harus diatur:
        - **X₁ = {opt['x1']:.2f}**
        - **X₂ = {opt['x2']:.2f}**
        - **Nilai Z optimal = {opt['z']:.2f}**
        """)

    else:
        st.info("👈 Silakan input masalah program linier di sidebar, lalu klik **🚀 HITUNG SOLUSI OPTIMAL**")
        
        col_info1, col_info2 = st.columns(2)
        
        with col_info1:
            with st.container(border=True):
                st.markdown("""
                #### 📖 Tentang Program
                
                Program ini menyelesaikan masalah **Optimasi Program Linier** 
                dengan 2 variabel menggunakan **Metode Grafis (Geometris)**.
                
                Cocok untuk kasus:
                - Maksimasi keuntungan
                - Minimasi biaya
                - Alokasi sumber daya terbatas
                """)
        
        with col_info2:
            with st.container(border=True):
                st.markdown("""
                #### 🎯 Fitur Utama
                
                - ✅ Input dinamis (fungsi tujuan & kendala)
                - ✅ 4 contoh kasus siap pakai
                - ✅ Input nama kasus custom
                - ✅ Visualisasi grafik feasible region
                - ✅ Tabel titik ekstrim otomatis
                - ✅ Support Maksimasi & Minimasi
                """)
        
        with st.container(border=True):
            st.markdown("""
            #### 🧮 Langkah Metode Grafis:
            
            1. **Gambar sumbu koordinat** X₁ dan X₂
            2. **Gambar garis** dari setiap fungsi kendala
            3. **Tentukan daerah fisibel** (feasible region) — daerah yang memenuhi semua kendala
            4. **Cari titik-titik ekstrim** (titik pojok) daerah fisibel
            5. **Hitung nilai Z** pada setiap titik ekstrim
            6. **Pilih titik dengan nilai Z terbaik** sebagai solusi optimal
            """)


if __name__ == "__main__":
    main()