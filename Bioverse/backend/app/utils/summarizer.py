from transformers import pipeline

# Initialize summarizer once
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    print("⚠️ Could not load summarization model:", e)
    summarizer = None

def summarize_text(text: str, max_len: int = 120, min_len: int = 30) -> str:
    """
    Summarize text using pretrained model.
    """
    if not summarizer or not text.strip():
        return text[:500]  # fallback: return truncated text

    try:
        result = summarizer(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )
        return result[0]["summary_text"]
    except Exception as e:
        print("Summarization failed:", e)
        return text[:500]

