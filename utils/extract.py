import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}


def fetching_content(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error saat request ke {url}: {e}")
        return None


def extract_product_data(card):
    try:
        # Title
        title_tag = card.find('h3', class_='product-title')
        title = title_tag.get_text(strip=True) if title_tag else None

        # Price
        price_tag = card.find(class_='price')
        price = price_tag.get_text(strip=True) if price_tag else None

        # Details (Rating, Colors, Size, Gender)
        p_tags = card.find_all('p')

        rating, colors, size, gender = None, None, None, None

        for p in p_tags:
            text = p.get_text(strip=True).lower()

            if "rating" in text:
                rating = text.split(":")[-1].strip()

            elif "color" in text:
                colors = ''.join(filter(str.isdigit, text))

            elif "size" in text:
                size = text.split(":")[-1].strip()

            elif "gender" in text:
                gender = text.split(":")[-1].strip()

        return {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender
        }

    except Exception:
        return None


def scrape_fashion(base_url, max_pages=50, delay=2):
    data = []

    for page in range(1, max_pages + 1):
        # 🔥 handle URL pagination
        if page == 1:
            url = base_url
        else:
            url = f"{base_url}/page{page}"

        print(f"Scraping halaman {page}: {url}")

        content = fetching_content(url)
        if not content:
            break

        soup = BeautifulSoup(content, "html.parser")

        products = soup.find_all('div', class_='collection-card')

        # stop kalau halaman kosong
        if not products:
            print("Tidak ada produk, stop.")
            break

        for product in products:
            item = extract_product_data(product)
            if item:
                data.append(item)

        time.sleep(delay)

    return data


def save_to_csv(data, filename="fashion_studio_data.csv"):
    df = pd.DataFrame(data)
    df = df.dropna(how="all")
    df.to_csv(filename, index=False)

    print(f"File tersimpan: {filename} | total data: {len(df)}")
    return df


# ===== MAIN =====
if __name__ == "__main__":
    base_url = "https://fashion-studio.dicoding.dev"

    data = scrape_fashion(base_url, max_pages=50, delay=2)

    save_to_csv(data)
