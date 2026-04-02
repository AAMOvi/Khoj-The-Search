# search_candidates.py
from .ngram import generate_ngrams
from .load_data import load_dataset

class SearchCandidates:
    def __init__(self, index, n=3):
        """
        index : the ngram index built by indexer.py
        n     : n-gram size
        """
        self.index = index
        self.n = n

    def get_candidates(self, query):
        """
        Return candidate restaurant IDs matching the query using n-grams.
        """
        query_ngrams = generate_ngrams(query, self.n)
        candidates = set()
        for ng in query_ngrams:
            if ng in self.index:
                candidates.update(self.index[ng])
        return candidates


# -------------------------
# Example Test
# -------------------------
if __name__ == "__main__":
    from indexer import NGramIndexer
    # Load dataset
    df = load_dataset()
    df['search_text'] = df['name'] + " " + df['address']

    # Build index
    indexer = NGramIndexer(n=3)
    ngram_index = indexer.build_index(df)

    # Initialize search
    searcher = SearchCandidates(ngram_index, n=3)

    # Example query
    query = "kacci bhai"
    candidate_ids = searcher.get_candidates(query)
    print(f"Candidate IDs for '{query}': {candidate_ids}")
    print("Example restaurant names:")
    print([df.iloc[i]['name'] for i in list(candidate_ids)[:5]])