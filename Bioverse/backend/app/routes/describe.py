from fastapi import APIRouter, Query
from app.database import DATA
from app.utils.summarizer import summarize_text

router = APIRouter(prefix="/describe", tags=["Describe"])

@router.get("/")
def describe(q: str = Query(..., description="Topic or keyword to summarize")):
    """
    Combine descriptions of top-matching datasets and return AI-generated summary.
    """
    q = q.lower()
    matched = [
        d for d in DATA
        if q in d["title"].lower()
        or q in d.get("description", "").lower()
        or any(q in kw.lower() for kw in d.get("keywords", []))
    ]

    if not matched:
        return {"query": q, "summary": "No matching data found.", "sources": []}

    # Combine top few descriptions
    combined_text = " ".join(d.get("description", "") for d in matched[:5])

    # Generate summary using AI
    summary = summarize_text(combined_text)

    return {
        "query": q,
        "summary": summary,
        "sources": matched[:5]
    }

