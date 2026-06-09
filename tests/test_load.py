import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import os
from utils.load import load_to_csv

def test_load_to_csv():
    df = pd.DataFrame({
        "Title": ["Test"],
        "Price": [1000],
        "Rating": [4.5],
        "Colors": [3],
        "Size": ["M"],
        "Gender": ["Men"]
    })

    filename = "test_output.csv"
    load_to_csv(df, filename)

    assert os.path.exists(filename)

    # cleanup (biar file gak numpuk)
    os.remove(filename)
