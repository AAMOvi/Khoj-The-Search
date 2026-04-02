from rapidfuzz import fuzz
import math
import re


class Ranker:
    def __init__(self, df):
        """
        df columns expected:
        - name
        - rating
        - number_of_reviews
        """
        self.df = df

    def clean_text(self, text):
        text = str(text).lower().strip()
        text = re.sub(r"\s+", " ", text)
        return text

    def normalize_text(self, text):
        """
        General query/name normalization.
        Keeps this generic, not tied to any one brand.
        """
        text = self.clean_text(text)

        replacements = {
            "vai": "bhai",
            "vaii": "bhai",
            "bhaii": "bhai",
            "kacci": "kacchi",
            "khacci": "kacchi",
            "khacchi": "kacchi",
            "kachi": "kacchi",
            "katchi": "kacchi",
            "birani": "biryani",
            "biryani": "biryani",
        }

        words = text.split()
        words = [replacements.get(w, w) for w in words]
        return " ".join(words)

    def token_coverage_score(self, query, name):
        """
        Measures how many query words are meaningfully covered by the candidate name.
        This helps 'kacchi bhai' beat 'vai vai', because both words match better.
        """
        query_words = query.split()
        name_words = name.split()

        if not query_words:
            return 0

        matched = 0

        for qw in query_words:
            best = 0
            for nw in name_words:
                score = fuzz.ratio(qw, nw)
                if score > best:
                    best = score
            if best >= 75:
                matched += 1

        coverage_ratio = matched / len(query_words)
        return coverage_ratio * 25

    def exact_token_boost(self, query, name):
        """
        Small boost if normalized query words appear exactly in the normalized candidate.
        """
        query_words = query.split()
        name_words = set(name.split())

        exact_matches = sum(1 for w in query_words if w in name_words)
        return exact_matches * 6

    def prefix_boost(self, query, name):
        """
        Boost if candidate begins with the query or its first important token.
        """
        if not query:
            return 0

        boost = 0

        if name.startswith(query):
            boost += 12

        query_words = query.split()
        if query_words and name.startswith(query_words[0]):
            boost += 6

        return boost

    def popularity_score(self, rating, reviews):
        """
        Popularity should help, but not dominate text relevance.
        """
        rating = float(rating or 0)
        reviews = float(reviews or 0)

        rating_part = rating * 2.5
        review_part = math.log1p(reviews) * 2.0

        return rating_part + review_part

    def rank_candidates(self, candidate_ids, query, top_n=10):
        query_raw = self.clean_text(query)
        query_norm = self.normalize_text(query_raw)

        results = []

        for idx in candidate_ids:
            row = self.df.iloc[idx]

            raw_name = str(row["name"])
            name_clean = self.clean_text(raw_name)
            name_norm = self.normalize_text(raw_name)

            rating = row.get("rating", 0)
            reviews = row.get("number_of_reviews", 0)

            # --- Core fuzzy signals ---
            ratio_score = fuzz.ratio(query_norm, name_norm)
            partial_score = fuzz.partial_ratio(query_norm, name_norm)
            token_sort_score = fuzz.token_sort_ratio(query_norm, name_norm)
            token_set_score = fuzz.token_set_ratio(query_norm, name_norm)

            # Weighted text relevance
            text_score = (
                0.20 * ratio_score +
                0.30 * partial_score +
                0.20 * token_sort_score +
                0.30 * token_set_score
            )

            # Filter out weak matches early
            if text_score < 35:
                continue

            # --- Structural signals ---
            coverage_boost = self.token_coverage_score(query_norm, name_norm)
            exact_boost = self.exact_token_boost(query_norm, name_norm)
            prefix = self.prefix_boost(query_norm, name_norm)

            # --- Popularity ---
            popularity = self.popularity_score(rating, reviews)

            # Final score
            final_score = (
                text_score +
                coverage_boost +
                exact_boost +
                prefix +
                popularity
            )

            results.append((idx, round(final_score, 2)))

        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_n]