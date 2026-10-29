# 🧠 MindTrack: Daily Wellness & Analytics Companion

MindTrack is a comprehensive, modular wellness and mood-tracking application designed to bridge quantitative daily check-ins with qualitative natural language processing (NLP). Built with a robust Python backend and a modern self-contained web dashboard, MindTrack empowers users to track sleep, workload, stress, and mood over a 90-day window, uncovering deep statistical correlations and emotional trends.

---

## 🚀 Key Features

* **Structured Data Persistence (`storage.py`)**: Manages secure local JSON storage (`mindtrack_data.json`) with strict range validation (1–10 scale enforcement for metrics).
* **Statistical Modeling (`analytics_engine.py`)**: Computes Pearson correlation matrices ($r$) to identify primary mood drivers (sleep, stress, workload) and applies 14-day linear regression slopes ($m$) to track metric trajectories (*Improving, Stable, Declining*).
* **Natural Language Text Mining (`sentiment_analyzer.py` & `topic_extractor.py`)**: 
  * Utilizes NLTK's VADER sentiment analyzer for compound polarity scoring (-1.0 to +1.0).
  * Performs frequency mapping via `collections.Counter` to categorize journal themes into custom tags: **exams**, **fatigue**, **social**, and **workload**.
* **Unified Orchestration (`insight_generator.py`)**: Synthesizes statistical analytics and NLP summaries into actionable, plain-English insights.
* **Modern Web Dashboard (`index.html`)**: A production-ready, responsive single-file dashboard featuring LocalStorage persistence, JSON export/import, dynamic charts, and live client-side analytics.

---

## 🗂️ Project Architecture & File Structure

```text
MindTrack/
│
├── storage.py              # Schema validation, file I/O, and JSON persistence
├── generate_mock_data.py   # Synthetic 90-day test dataset generator
├── data_pipeline.py        # Pandas DataFrame transformation & moving averages
├── analytics_engine.py     # Pearson correlation & Linear Regression models
├── sentiment_analyzer.py   # NLTK VADER sentiment scoring module
├── topic_extractor.py      # Keyword categorization & theme extraction
├── insight_generator.py    # Master orchestration report generator
├── test_devc.py            # Integration test suite for NLP and topic mapping
└── index.html              # Production-ready web UI for Vercel deployment
