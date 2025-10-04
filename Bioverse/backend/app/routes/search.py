from fastapi import APIRouter, Query
from app.database import DATA

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/")
def search_datasets(q: str = Query(..., description="Search keyword")):
    q = q.lower()
    results = [
        d for d in DATA
        if q in d["title"].lower()
        or q in d.get("description", "").lower()
        or any(q in kw.lower() for kw in d.get("keywords", []))
    ]
    return {"count": len(results), "results": results}

