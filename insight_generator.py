
from sentiment_analyzer import analyze_journal_entry
from topic_extractor import extract_topics


def generate_insights(journal_text, analytics_summary=None):
    """
    Combine journal sentiment, topics, and optional
    statistical insights from Dev B's analytics module.
    """

    sentiment_result = analyze_journal_entry(journal_text)
    topic_result = extract_topics(journal_text)

    sentiment = sentiment_result["sentiment"]
    score = sentiment_result["compound"]
    dominant_topics = topic_result["dominant_topics"]

    if dominant_topics:
        topics_text = ", ".join(dominant_topics)
    else:
        topics_text = "No dominant theme identified"

    report = {
        "sentiment": sentiment,
        "sentiment_score": score,
        "dominant_topics": dominant_topics,
        "topic_counts": topic_result["topic_counts"],
        "analytics": analytics_summary,
        "summary": (
            f"Journal sentiment is {sentiment}. "
            f"Common journal theme: {topics_text}."
        )
    }

    return report


if __name__ == "__main__":
    journal = input("Enter your journal entry: ")

    result = generate_insights(journal)

    print("\n--- MindTrack Insights ---")
    print("Sentiment:", result["sentiment"])
    print("Sentiment score:", result["sentiment_score"])
    print("Dominant topics:", result["dominant_topics"])
    print("Topic counts:", result["topic_counts"])
    print("Summary:", result["summary"])
