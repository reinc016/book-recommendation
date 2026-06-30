import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class RecommenderService:
    def __init__(self):
        self.base_path = "data"
        self.books = None
        self.ratings = None
        self.cosine_sim = None # Will store the similarity matrix

    def load_data(self):
        if self.books is None:
            self.books = pd.read_csv(os.path.join(self.base_path, "Books.csv"))
            self.ratings = pd.read_csv(
                os.path.join(self.base_path, "ratings.csv"),
                usecols=['user_id', 'book_id', 'rating']
            )
            
            # 1. Feature Engineering: Combine Title and Author
            self.books['combined_features'] = self.books['Title'].fillna('') + " " + self.books['Author'].fillna('')
            
            # 2. Vectorization: Converting text to numbers
            tfidf = TfidfVectorizer(stop_words='english')
            tfidf_matrix = tfidf.fit_transform(self.books['combined_features'])
            
            # 3. Similarity: The core algorithm
            self.cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
            print("Data loaded and similarity matrix computed.")

    def get_user_recommendations(self, user_id: int):
        # Your existing history lookup logic
        user_ratings = self.ratings[self.ratings['user_id'] == user_id]
        return user_ratings.merge(self.books, on='book_id').to_dict(orient="records")

    def get_similar_books(self, book_id: int):
        # Algorithm: Find books similar to the one provided
        idx = self.books.index[self.books['book_id'] == book_id].tolist()[0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
        book_indices = [i[0] for i in sim_scores]
        return self.books.iloc[book_indices].to_dict(orient="records")

recommender = RecommenderService()
