# ngram.py
def generate_ngrams(text, n=3):
    """
    Generate n-grams from a given string.
    Example:
        text = "kacchi bhai"
        n = 3
        output = ['kac', 'acc', 'cch', 'chi', 'hi ', 'i b', ' bh', 'bha', 'hai']
    """
    text = text.lower()  # lowercase for case-insensitive search
    text = text.replace("  ", " ")  # normalize double spaces
    text = f" {text} "  # pad spaces at start and end
    ngrams = [text[i:i+n] for i in range(len(text)-n+1)]
    return ngrams


# -------------------------
# Example Test
# -------------------------
if __name__ == "__main__":
    test_text = "kacchi bhai"
    ngrams = generate_ngrams(test_text, n=3)
    print("Text:", test_text)
    print("3-grams:", ngrams)