from fastapi import FastAPI
from app.services.recommender import recommender
from app.routers import recommendations  # 1. Import your router

app = FastAPI()

# Register your router
app.include_router(recommendations.router, prefix="/api")  # 2. Add this line

@app.on_event("startup")
async def startup_event():
    print("Loading datasets into memory...")
    recommender.load_data()
    print("System ready!")

@app.get("/")
def read_root():
    return {"message": "Book Recommendation API is online"}