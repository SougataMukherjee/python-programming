import pandas as pd

def load_csv(file):
    return pd.read_csv(file)

def map_sentiment_to_category(sentiment_text: str) -> str:
    """Map LLM output to predefined categories."""
    sentiment_text = sentiment_text.lower()
    if "happy" in sentiment_text or "positive" in sentiment_text:
        return "Happy 😀"
    elif "moderate" in sentiment_text:
        return "Moderate 🙂"
    elif "ok" in sentiment_text:
        return "OkOk 😐"
    elif "bad" in sentiment_text or "negative" in sentiment_text:
        return "Bad 😡"
    else:
        return "Unknown 🤔"
