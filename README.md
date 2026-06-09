# ETL Pipeline Fashion Studio Data

Proyek ini merupakan implementasi **ETL (Extract, Transform, Load) Pipeline** menggunakan Python untuk mengumpulkan data produk fashion dari website Fashion Studio, membersihkan data yang diperoleh, dan menyimpannya ke dalam format CSV.

Pipeline dibangun secara modular dengan memisahkan proses:

- Extract → Web Scraping data produk
- Transform → Data Cleaning & Data Validation
- Load → Penyimpanan data ke file CSV

Selain itu, proyek ini juga dilengkapi dengan **unit testing** untuk memastikan setiap proses berjalan dengan benar.

## Tujuan Proyek

- Mengotomatisasi pengambilan data dari website.
- Membersihkan data yang tidak valid.
- Menghasilkan dataset yang siap digunakan untuk analisis lebih lanjut.
- Menerapkan konsep ETL Pipeline yang umum digunakan pada Data Engineering.

## Struktur Proyek

```text
submission-pemda/
│
├── main.py
├── requirements.txt
├── fashion_studio_data.csv
├── submission.txt
│
├── utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
└── tests/
    ├── test_extract.py
    ├── test_transform.py
    └── test_load.py
```

## ETL Workflow

### 1. Extract

Mengambil data produk dari website menggunakan:

- Requests
- BeautifulSoup

Data yang diambil meliputi:

- Product Title
- Price
- Rating
- Number of Colors
- Size
- Gender

Fitur:

- Multi-page scraping
- Error handling untuk request gagal
- User-Agent configuration
- Delay antar request

### 2. Transform

Tahap pembersihan data meliputi:

#### Data Validation

Menghapus data yang tidak valid seperti:

- Unknown Product
- Price Unavailable
- Invalid Rating
- Not Rated

#### Data Cleaning

- Konversi harga ke format numerik
- Konversi harga USD ke Rupiah
- Membersihkan nilai rating
- Membersihkan jumlah warna
- Standardisasi Size dan Gender
- Menghapus data duplikat
- Menghapus missing values

#### Data Enrichment

- Menambahkan timestamp proses ETL

### 3. Load

Data yang telah bersih disimpan ke file:

```text
fashion_studio_data.csv
```

## Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Requests
- BeautifulSoup4
- Pytest

## Instalasi

Clone repository:

```bash
git clone https://github.com/username/repository-name.git
```

Masuk ke folder project:

```bash
cd repository-name
```

Install dependencies:

```bash
pip install -r requirements.txt
```
## Menjalankan Pipeline

Jalankan ETL Pipeline:

```bash
python main.py
```

Output:

```text
fashion_studio_data.csv
```

## Menjalankan Unit Test

Menjalankan seluruh test:

```bash
pytest
```

## Test Coverage

Melihat coverage testing:

```bash
pytest --cov=utils tests
```

## Dataset Output

Kolom hasil akhir:

| Column | Description |
|----------|-------------|
| Title | Nama produk |
| Price | Harga produk (Rupiah) |
| Rating | Rating produk |
| Colors | Jumlah warna tersedia |
| Size | Ukuran produk |
| Gender | Target gender |
| Timestamp | Waktu proses ETL |

## Skills Demonstrated

- Web Scraping
- Data Cleaning
- ETL Pipeline Development
- Modular Programming
- Unit Testing
- Data Engineering Fundamentals
- Error Handling
- Data Validation
