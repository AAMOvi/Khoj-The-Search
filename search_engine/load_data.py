import pandas as pd
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "dataset" / "khoj_restaurants.csv"

def load_dataset():
    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")
    df["search_text"] = df["name"].astype(str) + " " + df["address"].astype(str)
    return df

def load_dataset():
    df = pd.read_csv("Data/khoj_restaurants.csv", encoding="utf-8-sig")

    # Keep only needed columns
    df = df[['name', 'address', 'rating', 'number_of_reviews', 'affluence']]

    # Create search_text for n-gram indexing
    df['search_text'] = df['name'].astype(str) + " " + df['address'].astype(str)

    return df


# -------------------------
# Quick test
# -------------------------
if __name__ == "__main__":
    df = load_dataset()
    print(df[['name','search_text']].head())