from fastapi import APIRouter, Query
from app.database import DATA
from app.utils.classifier import recommend_similar

router = APIRouter(prefix="/recommend", tags=["Recommendations"])

@router.get("/")
def recommend(q: str = Query(..., description="Query keyword or ID")):
    return recommend_similar(DATA, q)

