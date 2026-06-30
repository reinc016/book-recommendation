from pydantic import BaseModel, Field

# Base schema for core book details (Used by Similarity endpoint)
class BookBase(BaseModel):
    book_id: int
    title: str = Field(alias='Title')
    author: str = Field(alias='Author')

    class Config:
        populate_by_name = True
        from_attributes = True

# Extended schema for user-specific data (Used by Recommendation endpoint)
class BookRecommendation(BookBase):
    user_id: int
    rating: int