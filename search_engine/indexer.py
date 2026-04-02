# indexer.py
from collections import defaultdict
from .ngram import generate_ngrams

class NGramIndexer:
    def __init__(self, n=3):
        self.n = n
        self.index = defaultdict(set)  # ngram -> set of restaurant IDs

    def build_index(self, df):
        """
        Build n-gram index from the dataframe.
        df must have 'search_text' column.
        """
        for idx, text in df['search_text'].items():
            ngrams = generate_ngrams(text, self.n)
            for ng in ngrams:
                self.index[ng].add(idx)  # store restaurant ID
        return self.index

    def get_index(self):
        """Return the built index"""
        return self.index


# -------------------------
# Example Test
# -------------------------
if __name__ == "__main__":
    import pandas as pd
    from load_data import load_dataset

    # Load sample data
    df = load_dataset()

    # Build index
    indexer = NGramIndexer(n=3)
    ngram_index = indexer.build_index(df)

    # Test lookup
    test_ngram = 'kac'  # example ngram
    candidates = ngram_index.get(test_ngram, set())
    print(f"Candidates for '{test_ngram}': {candidates}")
    print(f"Example restaurant names: {[df.iloc[i]['name'] for i in list(candidates)[:5]]}")