import re
from typing import Optional, Union, List, Dict
import pandas as pd
import numpy as np
from datetime import datetime


def clean_data(raw_data: List[Dict]) -> pd.DataFrame:
    df = pd.DataFrame(raw_data)

    expected_cols = ["Title", "Price", "Rating", "Colors", "Size", "Gender"]
    for c in expected_cols:
        if c not in df.columns:
            df[c] = None

    # === FILTER INVALID DATA ===
    # Hapus Title = "Unknown Product"
    df = df[df["Title"].astype(str).str.lower() != "unknown product"]

    # Hapus Price = "Price Unavailable"
    df = df[~df["Price"].astype(str).str.contains("price unavailable", case=False, na=False)]

    # Hapus Rating = "Invalid Rating / 5" atau "Not Rated"
    df = df[~df["Rating"].astype(str).str.contains("invalid rating", case=False, na=False)]
    df = df[~df["Rating"].astype(str).str.contains("not rated", case=False, na=False)]

    # === PRICE ===
    # Hapus karakter non-numerik (misal "$", ",", spasi) lalu konversi ke Rupiah
    df["Price"] = df["Price"].astype(str).str.replace(r"[^\d.]", "", regex=True)
    df["Price"] = df["Price"].replace("", np.nan)
    df = df.dropna(subset=["Price"])
    df["Price"] = df["Price"].astype(float) * 16000  # konversi ke Rupiah (kurs 16.000)

    # === RATING ===
    # Ambil angka desimal dari string rating, lalu jadikan float
    def _parse_rating(val):
        if val is None:
            return None
        m = re.search(r"(\d+(\.\d+)?)", str(val))
        return float(m.group()) if m else None

    df["Rating"] = df["Rating"].apply(_parse_rating)
    df = df.dropna(subset=["Rating"])
    df["Rating"] = df["Rating"].astype(float)

    # === COLORS ===
    # extract.py sudah menyimpan digit saja, tapi jaga-jaga bersihkan lagi
    # Pastikan hanya angka (bukan "3 colors", dll.)
    df["Colors"] = df["Colors"].astype(str).str.replace(r"\D", "", regex=True)
    df["Colors"] = df["Colors"].replace("", np.nan)
    df = df.dropna(subset=["Colors"])
    df["Colors"] = df["Colors"].astype(int)

    # === SIZE ===
    # Hapus prefix "size:" kalau ada
    df["Size"] = df["Size"].astype(str).str.replace(r"(?i)size\s*:\s*", "", regex=True).str.strip()

    # === GENDER ===
    # Hapus prefix "gender:" kalau ada
    df["Gender"] = df["Gender"].astype(str).str.replace(r"(?i)gender\s*:\s*", "", regex=True).str.strip()

    # === DROP DUPLIKAT ===
    df = df.drop_duplicates()

    # === DROP BARIS YANG MASIH ADA NULL ===
    df = df.dropna()

    # === TAMBAH TIMESTAMP ===
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df["timestamp"] = timestamp

    # === URUTAN KOLOM FINAL ===
    df = df[["Title", "Price", "Rating", "Colors", "Size", "Gender", "timestamp"]]

    return df


def clean_products(data: Union[pd.DataFrame, List[Dict]]) -> pd.DataFrame:
    if isinstance(data, pd.DataFrame):
        return clean_data(data.to_dict(orient="records"))
    elif isinstance(data, list):
        return clean_data(data)
    else:
        raise TypeError("clean_products expects a pandas DataFrame or a list of dicts")
