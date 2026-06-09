import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from utils.transform import transform_data

def test_transform_data():
    data = {
        "Title": ["Test Product"],
        "Price": ["$100.00"],
        "Rating": ["⭐ 4.5 / 5"],
        "Colors": ["3 Colors"],
        "Size": ["Size: M"],
        "Gender": ["Gender: Men"]
    }

    df = pd.DataFrame(data)
    result = transform_data(df)

    assert not result.empty
    assert result["Price"].iloc[0] == 1600000.0
    assert result["Rating"].iloc[0] == 4.5
    assert result["Colors"].iloc[0] == 3
