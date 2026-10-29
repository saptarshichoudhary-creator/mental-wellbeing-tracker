
from sentiment_analyzer import analyze_journal_entry
from topic_extractor import extract_topics


journal = (
    "I am exhausted after studying for exams. "
    "I have assignments and a project deadline."
)

sentiment_result = analyze_journal_entry(journal)
topic_result = extract_topics(journal)

print("Journal:", journal)
print("Sentiment:", sentiment_result)
print("Topics:", topic_result)
