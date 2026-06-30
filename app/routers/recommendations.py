from fastapi import APIRouter, HTTPException
from typing import List
from app.services.recommender import recommender
from app.schemas.book import BookRecommendation, BookBase # Import both

router = APIRouter()

# Route 1: History-based (Requires user_id and rating)
@router.get("/recommend/{user_id}", response_model=List[BookRecommendation])
async def get_recommendations(user_id: int):
    results = recommender.get_user_recommendations(user_id)
    if not results:
        raise HTTPException(status_code=404, detail="User not found")
    return results

# Route 2: Similarity-based (Requires only metadata)
@router.get("/recommend/similar/{book_id}", response_model=List[BookBase])
async def get_similar(book_id: int):
    results = recommender.get_similar_books(book_id)
    if not results:
        raise HTTPException(status_code=404, detail="Similar books not found")
    return results