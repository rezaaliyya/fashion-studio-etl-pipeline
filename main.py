from utils.extract import scrape_fashion
from utils.transform import clean_products
from utils.load import load_to_csv


def main():
    base_url = "https://fashion-studio.dicoding.dev"

    # === EXTRACT ===
    print("=== Memulai proses ekstraksi data ===")
    raw_data = scrape_fashion(base_url, max_pages=50, delay=2)
    print(f"Total data mentah yang berhasil di-scrape: {len(raw_data)} produk\n")

    # === TRANSFORM ===
    print("=== Memulai proses transformasi data ===")
    df_clean = clean_products(raw_data)
    print(f"Total data bersih setelah transformasi: {len(df_clean)} produk\n")

    # === LOAD ===
    print("=== Menyimpan data ke CSV ===")
    load_to_csv(df_clean)

    print("\nPreview 5 baris pertama:")
    print(df_clean.head())


if __name__ == "__main__":
    main()