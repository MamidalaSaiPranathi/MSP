import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = list(enumerate(similarity[index]))
    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

st.title('🎬 Movie Recommendation System')
selected_movie = st.selectbox("Choose a movie", movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i, rec in enumerate(recommendations, 1):
        st.write(f"{i}. {rec}")

