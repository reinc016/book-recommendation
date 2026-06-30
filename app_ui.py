import streamlit as st
import requests
import pandas as pd

# 1. Load your CSV to get a map of Titles -> IDs
# (Assuming you have your books.csv in the same folder)
df = pd.read_csv('data/books.csv') 

st.title("📚 Book Recommender System")

# 2. Create a Searchable Dropdown
selected_title = st.selectbox("Search for a book:", df['Title'].unique())

# 3. Find the ID for the selected title
selected_id = df[df['Title'] == selected_title]['book_id'].values[0]

if st.button("Get Recommendations"):
    response = requests.get(f"http://127.0.0.1:8000/api/recommend/similar/{selected_id}")
    
    if response.status_code == 200:
        recommendations = response.json()
        st.write(f"### Books similar to '{selected_title}':")
        for book in recommendations:
            st.success(f"**{book['Title']}** by {book['Author']}")