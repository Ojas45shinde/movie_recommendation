import streamlit as st
import pickle
import pandas as pd
import requests
import time

def poster(movie_id):
    api_key = '7b995d3c6fd91a2284b4ad8cb390c7b8'  # Replace with your TMDB API key
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data["poster_path"]


def recommend(movie):

    movie_index =movies[movies["title"]== movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id

        
        recommended_movies.append((movies.iloc[i[0]].title))
        recommended_movies_posters.append(poster(movie_id))

    return recommended_movies,recommended_movies_posters


movies_dict=pickle.load(open("movies_dict.pkl",'rb'))
movies =pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender system")

selected_movie_name=st.selectbox(
    "Which movies would you like to choose?",movies['title'].values
)
if st.button("Recommend"):
    names,posters=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.subheader(names[0])
        st.image(posters[0])

    with col2:
        st.subheader(names[1])
        st.image(posters[1])

    with col3:
        st.subheader(names[2])
        st.image(posters[2])   
        
    with col4:
        st.subheader(names[3])
        st.image(posters[3])  
          
    with col5:
        st.subheader(names[4])
        st.image(posters[4])