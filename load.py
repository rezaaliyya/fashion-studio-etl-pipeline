import pandas as pd


def load_to_csv(df: pd.DataFrame, filename: str = "fashion_studio_data.csv") -> None:
    df.to_csv(filename, index=False)
    print(f"File tersimpan: {filename}")
    print(f"Total data: {len(df)} produk")