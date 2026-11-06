import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import os
import glob

# Konfigurasi halaman
st.set_page_config(
    page_title="Air Quality Dashboard",
    page_icon="🌫️",
    layout="wide"
)

# Tema grafik
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titleweight": "bold",
    "axes.titlesize": 12,
    "grid.color": "#E5E7EB",
})

# Custom Styling
st.markdown("""
<style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    /* Banner judul */
    .hero {
        background: linear-gradient(120deg, #24445C 0%, #315D75 60%, #3F8FA8 100%);
        padding: 24px 30px;
        border-radius: 14px;
        color: white;
        margin-bottom: 20px;
    }
    .hero h1 {
        color: white;
        margin: 0;
        padding: 0;
        font-size: 2rem;
    }
    .hero p {
        margin: 6px 0 0 0;
        opacity: 0.9;
    }

    h2 {
        color: #24445C;
        font-size: 1.4rem !important;
        margin-top: 1rem;
    }

    /* Kartu metrik */
    div[data-testid="stMetric"] {
        background-color: white;
        padding: 16px 18px;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        border-left: 5px solid #315D75;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
    }

    div[data-testid="stDownloadButton"] button {
        background-color: #315D75;
        color: white;
        border-radius: 8px;
        border: none;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid #E5E7EB;
    }
</style>
""", unsafe_allow_html=True)

# Judul Dashboard
st.markdown("""
<div class="hero">
    <h1>Air Quality Dashboard</h1>
    <p>Analisis kualitas udara berdasarkan konsentrasi PM2.5 di Beijing pada periode 2013–2017.</p>
</div>
""", unsafe_allow_html=True)


# Membaca Dataset
@st.cache_data
def load_data():
    zip_path = "Air-quality-dataset.zip"
    extract_path = "data"

    # Mengekstrak file ZIP
    os.makedirs(extract_path, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)

    # Mencari seluruh file CSV
    csv_files = glob.glob(
        os.path.join(extract_path, "**", "*.csv"),
        recursive=True
    )

    # Membaca dan menggabungkan seluruh CSV
    dataframes = []

    for file in csv_files:
        temp_df = pd.read_csv(file)
        dataframes.append(temp_df)

    df = pd.concat(dataframes, ignore_index=True)

    return df


# Memuat dataset
try:
    df = load_data()
except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")
    st.stop()

# Membuat kolom datetime
df["datetime"] = pd.to_datetime(
    df[["year", "month", "day", "hour"]],
    errors="coerce"
)

# Filter Data (di sidebar)
with st.sidebar:
    st.header("Filter Data")

    station_list = ["Semua Stasiun"] + sorted(df["station"].unique().tolist())

    selected_station = st.selectbox(
        "Pilih Stasiun Pemantauan:",
        station_list
    )

# Terapkan filter
if selected_station == "Semua Stasiun":
    filtered_df = df.copy()
else:
    filtered_df = df[df["station"] == selected_station].copy()

# Data PM2.5 yang sudah difilter
filtered_pm25 = filtered_df.dropna(subset=["PM2.5"]).copy()

with st.sidebar:
    st.caption(f"Jumlah data yang ditampilkan: {len(filtered_df):,} observasi")

# Ringkasan Dataset
st.header("📊 Ringkasan Dataset")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Observasi",
        value=f"{len(df):,}"
    )

with col2:
    st.metric(
        label="Jumlah Stasiun",
        value=df["station"].nunique()
    )

with col3:
    st.metric(
        label="Periode Data",
        value=f"{df['year'].min()} - {df['year'].max()}"
    )

# Menampilkan Data
with st.expander("Lihat Data Mentah"):
    st.dataframe(df.head(10), use_container_width=True)

# Insight dan Ringkasan Analisis
st.header("💡 Insight Analisis")

# Mengambil data PM2.5 yang tersedia
pm25_values = filtered_df["PM2.5"].dropna()

if not pm25_values.empty:

    # Menghitung statistik
    avg_pm25 = pm25_values.mean()
    median_pm25 = pm25_values.median()
    max_pm25 = pm25_values.max()
    min_pm25 = pm25_values.min()

    # Mencari waktu konsentrasi tertinggi
    peak_row = filtered_df.loc[filtered_df["PM2.5"].idxmax()]
    peak_date = peak_row["datetime"].strftime("%d %B %Y, %H:%M")

    # Menampilkan metrik
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rata-rata PM2.5", f"{avg_pm25:.2f} µg/m³")
    col2.metric("Median PM2.5", f"{median_pm25:.2f} µg/m³")
    col3.metric("PM2.5 Tertinggi", f"{max_pm25:.2f} µg/m³")
    col4.metric("PM2.5 Terendah", f"{min_pm25:.2f} µg/m³")

    # Menampilkan penjelasan
    if selected_station == "Semua Stasiun":
        station_description = "seluruh stasiun pemantauan"
    else:
        station_description = f"stasiun {selected_station}"

    st.info(
        f"""
**Temuan utama:**

- Rata-rata konsentrasi PM2.5 pada {station_description} adalah **{avg_pm25:.2f} µg/m³**.
- Konsentrasi tertinggi yang tercatat adalah **{max_pm25:.2f} µg/m³**, pada {peak_date}.
- Konsentrasi terendah yang tercatat adalah **{min_pm25:.2f} µg/m³**.
        """
    )

    # Detail Konsentrasi PM2.5 Tertinggi
    with st.expander("Lihat Detail Observasi PM2.5 Tertinggi"):
        st.write("Detail observasi dengan konsentrasi PM2.5 tertinggi:")

        st.dataframe(
            peak_row[
                ["station", "datetime", "PM2.5", "PM10",
                 "SO2", "NO2", "CO", "O3"]
            ].astype(str).to_frame(name="Nilai"),
            use_container_width=True
        )

else:
    st.warning("Tidak tersedia data PM2.5 untuk pilihan ini.")

# Grafik Rata-rata PM2.5 per Stasiun
st.header("📊 Rata-rata PM2.5 per Stasiun")

# Menghitung rata-rata PM2.5
station_pm25 = (
    df.groupby("station")["PM2.5"]
    .mean()
    .sort_values(ascending=False)
)

# Membuat grafik
fig, ax = plt.subplots(figsize=(10, 4))

sns.barplot(
    x=station_pm25.values,
    y=station_pm25.index,
    color="#315D75",
    ax=ax
)

ax.set_title("Rata-rata Konsentrasi PM2.5 per Stasiun")
ax.set_xlabel("Rata-rata PM2.5 (µg/m³)")
ax.set_ylabel("")

plt.tight_layout()

with st.container(border=True):
    st.pyplot(fig)
plt.close(fig)

# Grafik Tren PM2.5 per Bulan
st.header("📈 Tren Rata-rata PM2.5 per Bulan")

# Menghitung rata-rata PM2.5 berdasarkan filter stasiun
monthly_pm25 = (
    filtered_pm25.groupby(
        filtered_pm25["datetime"].dt.to_period("M")
    )["PM2.5"]
    .mean()
)

monthly_pm25.index = monthly_pm25.index.to_timestamp()

# Membuat grafik
fig, ax = plt.subplots(figsize=(12, 4))

ax.plot(
    monthly_pm25.index,
    monthly_pm25.values,
    color="#F97316",
    linewidth=2
)
ax.fill_between(
    monthly_pm25.index,
    monthly_pm25.values,
    color="#F97316",
    alpha=0.12
)

ax.set_title("Tren Rata-rata Konsentrasi PM2.5 per Bulan")
ax.set_xlabel("Bulan")
ax.set_ylabel("Rata-rata PM2.5 (µg/m³)")

plt.xticks(rotation=45)
plt.tight_layout()

with st.container(border=True):
    st.pyplot(fig)
plt.close(fig)

# Distribusi PM2.5 Berdasarkan Kuartil
st.header("📊 Distribusi PM2.5 Berdasarkan Kuartil")

# Mengambil data PM2.5 yang tidak kosong
pm25_data = filtered_df["PM2.5"].dropna()

# Membagi data menjadi empat kuartil
pm25_category = pd.qcut(
    pm25_data,
    q=4,
    labels=["Kuartil 1", "Kuartil 2", "Kuartil 3", "Kuartil 4"]
)

# Menghitung jumlah data setiap kuartil
category_counts = pm25_category.value_counts().sort_index()

# Membuat grafik
fig, ax = plt.subplots(figsize=(8, 4))

category_counts.plot(
    kind="bar",
    color="#0D9488",
    ax=ax
)

ax.set_title("Distribusi Observasi PM2.5 Berdasarkan Kuartil")
ax.set_xlabel("Kategori Konsentrasi PM2.5")
ax.set_ylabel("Jumlah Observasi")
ax.tick_params(axis="x", rotation=0)

plt.tight_layout()

with st.container(border=True):
    st.pyplot(fig)
plt.close(fig)

st.caption(
    "Catatan: Kuartil merupakan pembagian berdasarkan distribusi data, "
    "bukan kategori resmi indeks kualitas udara (AQI)."
)

# Tabel Data Berdasarkan Filter
st.header("📋 Data Kualitas Udara")

st.write(
    f"Menampilkan data dari: **{selected_station}**"
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)

st.write(
    f"Total data: {len(filtered_df):,} observasi"
)

# Tombol Download CSV
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Data CSV",
    data=csv_data,
    file_name="air_quality_filtered.csv",
    mime="text/csv"
)

# Informasi Dataset
st.divider()

st.header("ℹ️ Tentang Dashboard")

st.markdown("""
Dashboard ini dibuat untuk menganalisis kualitas udara
di Beijing berdasarkan konsentrasi PM2.5.

**Informasi Dataset:**
- Nama dataset: Beijing Multi-Site Air Quality Data
- Lokasi: Beijing, China
- Jumlah stasiun: 12
- Periode pengamatan: Maret 2013 – Februari 2017
- Variabel utama: PM2.5

**Tujuan Analisis:**

1. Membandingkan rata-rata PM2.5 antarstasiun.
2. Mengamati perubahan konsentrasi PM2.5 setiap bulan.
3. Mengetahui distribusi konsentrasi PM2.5 berdasarkan kuartil.

**Catatan:**

Analisis ini bersifat deskriptif dan menggambarkan pola
konsentrasi PM2.5 berdasarkan data pengamatan.
Hasil analisis tidak digunakan untuk menyimpulkan
hubungan sebab-akibat.

Sumber dataset: Beijing Multi-Site Air Quality Data.
Silakan cantumkan tautan sumber tempat dataset diunduh.
""")

st.caption(
    "Air Quality Dashboard | Data Analysis Project"
)