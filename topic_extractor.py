
import re
from collections import Counter


TOPIC_KEYWORDS = {
    "exams": [
        "exam", "exams", "test", "quiz", "study",
        "studying", "revision", "marks", "grades"
    ],
    "fatigue": [
        "tired", "exhausted", "sleep", "sleepy",
        "fatigue", "rest", "insomnia", "energy"
    ],
    "social": [
        "friends", "friend", "family", "lonely",
        "relationship", "people", "party", "social"
    ],
    "workload": [
        "assignment", "assignments", "deadline",
        "project", "projects", "workload", "busy",
        "pressure", "tasks", "work"
    ]
}


def extract_topics(text):
    """
    Identify journal themes using predefined keywords.
    Return category counts and dominant themes.
    """
    if not isinstance(text, str) or not text.strip():
        return {
            "topic_counts": {},
            "dominant_topics": []
        }

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    word_counts = Counter(words)

    topic_counts = {}

    for topic, keywords in TOPIC_KEYWORDS.items():
        count = sum(word_counts[keyword] for keyword in keywords)
        topic_counts[topic] = count

    highest_count = max(topic_counts.values(), default=0)

    if highest_count == 0:
        dominant_topics = []
    else:
        dominant_topics = [
            topic
            for topic, count in topic_counts.items()
            if count == highest_count
        ]

    return {
        "topic_counts": topic_counts,
        "dominant_topics": dominant_topics
    }


if __name__ == "__main__":
    journal = input("Enter your journal entry: ")
    result = extract_topics(journal)

    print("Topic Counts:", result["topic_counts"])
    print("Dominant Topics:", result["dominant_topics"])
