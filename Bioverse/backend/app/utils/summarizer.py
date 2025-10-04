from transformers import pipeline
import os
from pathlib import Path

# Initialize summarizer once with local cache
try:
    # Set cache directory to your project
    cache_dir = Path("models/bart-large-cnn")
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    summarizer = pipeline(
        "summarization", 
        model="facebook/bart-large-cnn",
        model_kwargs={"cache_dir": str(cache_dir)}
    )
    print("✅ Summarization model loaded successfully")
except Exception as e:
    print(f"⚠️ Could not load summarization model: {e}")
    print("⚠️ Using fallback truncation instead")
    summarizer = None

def summarize_text(text: str, max_len: int = 120, min_len: int = 30) -> str:
    """
    Summarize text using pretrained model.
    Falls back to truncation if model unavailable.
    """
    if not text or not text.strip():
        return "No content available to summarize."
    
    if not summarizer:
        return text[:500] + "..." if len(text) > 500 else text

    try:
        # Only summarize if text is long enough
        if len(text) < 100:
            return text
            
        result = summarizer(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )
        return result[0]["summary_text"]
    except Exception as e:
        print(f"❌ Summarization failed: {e}")
        return text[:500] + "..." if len(text) > 500 else text
