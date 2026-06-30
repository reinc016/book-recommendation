# Book Recommendation System

A robust, content-based book recommendation engine built using **FastAPI** and **Scikit-learn**. This project leverages natural language processing to suggest books based on title and author similarity.

## 🚀 Features
*   **Content-Based Filtering**: Uses `TfidfVectorizer` and cosine similarity to find books with similar metadata.
*   **RESTful API**: Built with **FastAPI** for high performance and easy integration.
*   **Modular Architecture**: Organized into services, schemas, and routers for scalability and maintainability.
*   **Environment Ready**: Includes `.gitignore` and `requirements.txt` to ensure clean, reproducible deployments.

## 🛠 Tech Stack
*   **Backend**: Python, FastAPI
*   **Data Processing**: Pandas, Scikit-learn
*   **Version Control**: Git/GitHub

## 📋 Project Structure
```text
book-recommendation/
├── app/
│   ├── routers/          # API endpoint definitions
│   ├── schemas/          # Data validation models
│   ├── services/         # Core recommendation logic
│   ├── main.py           # Application entry point
│   └── database.py       # Database connection/handling
├── data/                 # CSV datasets (Books, Ratings)
├── .gitignore            # Excludes virtual environments and temp files
└── requirements.txt      # Project dependencies

How to Run
1. Clone the repository
Bash
git clone https://github.com/reinc016/book-recommendation.git
cd book-recommendation

2. Set up a virtual environment
Bash
python -m venv bookvenv
# Activate it (Windows)
.\bookvenv\Scripts\activate


3. Install dependencies
Bash
pip install -r requirements.txt


4. Run the application
Bash
uvicorn app.main:app --reload
The API will be live at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
