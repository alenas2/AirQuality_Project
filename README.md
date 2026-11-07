# Air Quality Analysis Dashboard

## Deskripsi Proyek

Proyek ini merupakan analisis data kualitas udara di Beijing, China, menggunakan dataset Beijing Multi-Site Air Quality Data. Analisis berfokus pada konsentrasi PM2.5 untuk mengetahui perbedaan kualitas udara antarstasiun pemantauan dan perubahan konsentrasinya dari waktu ke waktu.

Hasil analisis disajikan dalam bentuk notebook Jupyter dan dashboard interaktif menggunakan Streamlit.

## Dataset

**Link Dashboard:** https://air-quality-analysis-project-byalen.streamlit.app/ 

## Dataset

- **Nama:** Beijing Multi-Site Air Quality Data
- **Lokasi:** Beijing, China
- **Jumlah stasiun:** 12 stasiun pemantauan
- **Periode:** Maret 2013 – Februari 2017
- **Jumlah observasi:** 420.768 baris setelah penggabungan data
- **Variabel utama:** PM2.5

Dataset mentah terdiri dari 12 file CSV yang masing-masing merepresentasikan data dari satu stasiun pemantauan. File-file tersebut digunakan dalam proses analisis pada notebook.

## Pertanyaan Analisis

1. Bagaimana perbandingan rata-rata konsentrasi PM2.5 pada setiap stasiun pemantauan?
2. Bagaimana tren rata-rata konsentrasi PM2.5 setiap bulan selama periode 2013–2017?

## Hasil Analisis

- Rata-rata konsentrasi PM2.5 tertinggi berdasarkan stasiun ditemukan di Dongsi, sekitar 86,19 µg/m³.
- Rata-rata konsentrasi PM2.5 terendah ditemukan di Dingling, sekitar 65,99 µg/m³.
- Rata-rata bulanan tertinggi tercatat pada Desember 2015, sekitar 150,52 µg/m³.

## Fitur Dashboard

- Ringkasan dataset.
- Filter berdasarkan stasiun pemantauan.
- Grafik rata-rata PM2.5 per stasiun.
- Grafik tren rata-rata PM2.5 per bulan.
- Distribusi konsentrasi PM2.5 berdasarkan kuartil.
- Insight analisis.
- Tabel data kualitas udara.
- Download data hasil filter dalam format CSV.

## Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook / Google Colab

## Cara Menjalankan Proyek

### 1. Clone atau unduh repository

git clone [URL_REPOSITORY_GITHUB]
cd AirQuality_Project

### 2. Buat virtual environment

python -m venv .venv

### 3. Aktifkan virtual environment

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

### 4. Instal library

pip install -r requirements.txt

### 5. Jalankan dashboard

streamlit run dashboard/dashboard.py

Dashboard akan terbuka melalui browser pada alamat lokal yang ditampilkan di terminal.

## Struktur Folder

```text
AirQuality_Project/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── data/
│   ├── Data_Aotizhongxin.csv
│   ├── Data_Changping.csv
│   └── ... (10 file CSV lainnya)
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Catatan

Analisis ini bersifat deskriptif dan bertujuan menggambarkan pola konsentrasi PM2.5 berdasarkan data pengamatan. Hasil analisis tidak digunakan untuk menyimpulkan hubungan sebab-akibat.