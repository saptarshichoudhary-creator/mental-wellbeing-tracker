

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def load_analyzer():
    """Load VADER sentiment analyzer."""
    try:
        return SentimentIntensityAnalyzer()
    except LookupError:
        nltk.download("vader_lexicon")
        return SentimentIntensityAnalyzer()


analyzer = load_analyzer()


def analyze_journal_entry(text):
    """
    Analyze a journal entry and return its sentiment score.
    The compound score ranges from -1.0 to +1.0.
    """
    if not isinstance(text, str) or not text.strip():
        return {
            "compound": 0.0,
            "sentiment": "neutral"
        }

    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "positive"
    elif compound <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "compound": compound,
        "sentiment": sentiment
    }


if __name__ == "__main__":
    journal = input("Enter your journal entry: ")
    result = analyze_journal_entry(journal)

    print("Sentiment Score:", result["compound"])
    print("Sentiment:", result["sentiment"])
