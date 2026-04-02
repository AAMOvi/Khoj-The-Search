# search.py

from .load_data import load_dataset
from .indexer import NGramIndexer
from .search_candidates import SearchCandidates
from .ranking import Ranker


class KhojSearchEngine:

    def __init__(self):

        # Load dataset
        self.df = load_dataset()

        # Create search text
        self.df['search_text'] = self.df['name'] + " " + self.df['address']

        # Build N-Gram index
        indexer = NGramIndexer(n=3)
        self.index = indexer.build_index(self.df)

        # Candidate finder
        self.candidate_finder = SearchCandidates(self.index, n=3)

        # Ranker
        self.ranker = Ranker(self.df)


    def search(self, query, top_n=10):

        # Step 1: Find candidate IDs
        candidate_ids = self.candidate_finder.get_candidates(query)

        # Step 2: Rank candidates
        ranked = self.ranker.rank_candidates(candidate_ids, query, top_n)

        # Step 3: Prepare final results
        results = []

        for idx, score in ranked:
            row = self.df.iloc[idx]

            results.append({
                "name": row["name"],
                "address": row["address"],
                "rating": float(row["rating"]),
                "reviews": int(row["number_of_reviews"]),
                "score": round(score,2)
            })

        return results


# -------------------------
# Test the search engine
# -------------------------

if __name__ == "__main__":

    engine = KhojSearchEngine()

    query = "kacci bhai".lower()

    results = engine.search(query)

    print("\nSearch Results:\n")

    for r in results:
        print(r)