import streamlit as st
import pickle
import requests
import pandas as pd

def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}",
        params={
            "api_key": "f0fae71cba04d7904d15347e4eb6d9d5"
        },
        timeout=10
    )

    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movie = []
    recommended_movie_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie.append(
            movies.iloc[i[0]].title
        )

        recommended_movie_poster.append(
            fetch_poster(movie_id)
        )

    return recommended_movie, recommended_movie_poster


# Load movie data
movies = pickle.load(open('movie_dcit.pkl', 'rb'))

# Convert dictionary to DataFrame
movies = pd.DataFrame(movies)


# Load similarity matrix
similarity = pickle.load(open('movie_simi.pkl', 'rb'))
similarity = similarity.astype('float16')


# Streamlit UI
st.title('Movie Recommender System')


selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies['title'].values
)


if st.button('Recommend'):

    recommended_movie_names, recommended_movie_posters = recommend(
        selected_movie_name
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])

    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])

    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])

    with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])

    with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])