import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bs4 import BeautifulSoup
from utils.extract import extract_product_data

def test_extract_product_data():
    html = """
    <div class="collection-card">
        <div class="product-details">
            <h3 class="product-title">Test Product</h3>
            <span class="price">$100.00</span>
            <p>Rating: ⭐ 4.5 / 5</p>
            <p>3 Colors</p>
            <p>Size: M</p>
            <p>Gender: Men</p>
        </div>
    </div>
    """

    soup = BeautifulSoup(html, "html.parser")
    card = soup.find("div", class_="collection-card")

    result = extract_product_data(card)

    assert result is not None
    assert result["Title"] == "Test Product"
    assert result["Price"] == "$100.00"
