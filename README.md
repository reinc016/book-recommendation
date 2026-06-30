# 📚 AI Book Recommendation Engine

An AI-powered book recommendation system built with **FastAPI**, **Scikit-Learn**, and **Streamlit**. It uses **Content-Based Filtering** with **TF-IDF Vectorization** and **Cosine Similarity** to recommend books similar to the one you select.

---

## 🚀 Demo

Select any book from the dropdown → Click **Get Recommendations** → Get **5 similar books** instantly!

---

## 🧠 How It Works

1. The system loads the **Goodreads 10K Books** dataset on startup
2. Book **Title** and **Author** are combined into a single text feature
3. **TF-IDF Vectorizer** converts text into numerical vectors
4. **Cosine Similarity** is computed across all 10,000 books
5. When a book is selected, the **top 5 most similar books** are returned via REST API

---

## 🏗️ Project Structure

```
BOOK RECOMMENDATION/
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI entry point
│   ├── config.py                # Environment variables
│   ├── database.py              # DB setup (future use)
│   ├── routers/
│   │   └── recommendations.py  # API route handlers
│   ├── schemas/
│   │   └── book.py             # Pydantic schemas
│   └── services/
│       └── recommender.py      # ML engine (TF-IDF + Cosine Similarity)
├── data/
│   ├── Books.csv               # Book metadata (~10,000 records)
│   ├── Ratings.csv             # User ratings
│   └── to_read.csv             # User reading lists
├── app_ui.py                   # Streamlit frontend
├── requirements.txt            # Production dependencies
└── requirements.dev.txt        # Dev/audit tools
```

---

## ⚙️ Tech Stack

| **Layer** | **Technology** | **Purpose** |
|---|---|---|
| Backend | FastAPI + Uvicorn | REST API server |
| ML Engine | Scikit-Learn | TF-IDF vectorization + Cosine Similarity |
| Data Processing | Pandas | CSV loading, cleaning, merging |
| Schema Validation | Pydantic v2 | Request/response validation |
| Frontend | Streamlit | Interactive UI |
| Dataset | Goodreads 10K (Kaggle) | Book metadata + ratings |

---

## 📦 Installation

### **1. Clone the repository**

```bash
git clone https://github.com/reinc016/book-recommendation.git
cd book-recommendation
```

### **2. Create and activate virtual environment**

**Windows (PowerShell):**
```powershell
python -m venv bookvenv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\bookvenv\Scripts\Activate.ps1
```


### **3. Install dependencies**

```bash
pip install -r requirements.txt
```


## ▶️ Running the App

> **You need two terminals running simultaneously.**

### **Terminal 1 — Start FastAPI Backend**

```bash
uvicorn app.main:app --reload
```

- API live at: `http://127.0.0.1:8000`
- Interactive docs at: `http://127.0.0.1:8000/docs`

### **Terminal 2 — Start Streamlit Frontend**

```bash
streamlit run app_ui.py
```

- UI opens at: `http://localhost:8501`

---

## 🔌 API Endpoints

| **Method** | **Endpoint** | **Description** |
|---|---|---|
| `GET` | `/` | Health check |
| `GET` | `/api/recommend/{user_id}` | Get books from user's rating history |
| `GET` | `/api/recommend/similar/{book_id}` | Get 5 similar books using cosine similarity |

### **Example Response** — `/api/recommend/similar/1`

```json
[
  { "book_id": 2, "Title": "Catching Fire", "Author": "Suzanne Collins" },
  { "book_id": 3, "Title": "Mockingjay", "Author": "Suzanne Collins" },
  { "book_id": 4, "Title": "The Maze Runner", "Author": "James Dashner" },
  { "book_id": 5, "Title": "Divergent", "Author": "Veronica Roth" },
  { "book_id": 6, "Title": "The Giver", "Author": "Lois Lowry" }
]
```

---

## 🤖 ML Algorithm

```python
## Feature Engineering
books['combined_features'] = books['Title'] + " " + books['Author']

## TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books['combined_features'])

## Cosine Similarity Matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

## Get Top 5 Similar Books
sim_scores = sorted(
    enumerate(cosine_sim[idx]),
    key=lambda x: x[1],
    reverse=True
)[1:6]
```

---

## 📋 Dependencies

```
fastapi==0.138.1
uvicorn==0.49.0
sqlalchemy==2.0.51
aiosqlite==0.22.1
pandas==3.0.3
scikit-learn==1.9.0
passlib[bcrypt]==1.7.4
python-jose[cryptography]==3.5.0
python-multipart==0.0.32
pydantic==2.13.4
streamlit
```

---
## 🗂️ Dataset

| **File** | **Rows** | **Description** |
|---|---|---|
| `Books.csv` | ~10,000 | Book metadata (title, author, ISBN, rating, image URLs) |
| `Ratings.csv` | ~1,000,000 | User-book ratings (user\_id, book\_id, rating) |
| `to_read.csv` | — | Books users want to read |

> **Note:** Dataset files are **not included** in this repository due to size. Download from [Kaggle](https://www.kaggle.com/datasets/sahilkirpekar/goodreads10k-dataset-cleaned) and place in the `data/` folder.

