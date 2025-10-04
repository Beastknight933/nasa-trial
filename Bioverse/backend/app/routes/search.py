from fastapi import APIRouter, Query
from app.database import DATA
from app.models import Dataset

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/", response_model=dict)
def search(q: str = Query(..., description="Search keyword")):
    """
    Keyword-based search through title, description, and keywords.
    """
    q = q.lower()
    results = [
        d for d in DATA
        if q in d["title"].lower()
        or q in d.get("description", "").lower()
        or any(q in kw.lower() for kw in d.get("keywords", []))
    ]
    return {
        "query": q,
        "count": len(results),
        "results": results[:25]  # limit results for speed
    }

