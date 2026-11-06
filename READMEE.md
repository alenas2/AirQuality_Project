# Air Quality Analysis Dashboard

## Deskripsi Proyek

Proyek ini merupakan analisis data kualitas udara di Beijing, China, menggunakan dataset Beijing Multi-Site Air Quality Data. Analisis berfokus pada konsentrasi PM2.5 untuk mengetahui perbedaan kualitas udara antarstasiun pemantauan dan perubahan konsentrasinya dari waktu ke waktu.

Hasil analisis disajikan dalam bentuk notebook Jupyter dan dashboard interaktif menggunakan Streamlit.

## Dataset

- **Nama:** Beijing Multi-Site Air Quality Data
- **Lokasi:** Beijing, China
- **Jumlah stasiun:** 12 stasiun pemantauan
- **Periode:** Maret 2013 – Februari 2017
- **Jumlah observasi:** 420.768 baris
- **Variabel utama:** PM2.5

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

### 2. Buat virtual environment

```bash
python -m venv .venv
```

### 3. Aktifkan virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 4. Instal library

```bash
pip install -r requirements.txt
```

### 5. Jalankan dashboard

```bash
streamlit run dashboard.py
```

Dashboard akan terbuka melalui browser pada alamat lokal yang ditampilkan di terminal.

## Struktur Folder

```text
AirQuality_Project/
├── Air-quality-dataset.zip
├── notebook_analisis.ipynb
├── dashboard.py
├── requirements.txt
└── README.md
```

## Catatan

Analisis ini bersifat deskriptif dan bertujuan menggambarkan pola konsentrasi PM2.5 berdasarkan data pengamatan. Hasil analisis tidak digunakan untuk menyimpulkan hubungan sebab-akibat.