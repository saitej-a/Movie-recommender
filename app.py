import streamlit as st
import pickle as pk
import pandas as pd
import requests


movie_list=pk.load(open("moviesdata.pkl","rb"))
movies=pd.DataFrame(movie_list)
simularity=pk.load(open("simularity.pkl","rb"))
simularitydf=pd.DataFrame(simularity)

st.header("Movie recommender")
movie=st.selectbox(label="Choose the movie name",options=movies["title"].values)

def fetch(movie):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=872b4f07900bffe963fa08e318659170&language=en-US".format(movie))
    data=response.json()
    return "http://image.tmdb.org/t/p/w185"+data["poster_path"]
def recommend(movie):
    movie_id = movies[movies["title"] == movie].index[0]
    rec=[]
    pos=[]
    sim_movies = sorted(list(enumerate(simularity[movie_id])), reverse=True, key=lambda x: x[1])[1:11]
    for i in sim_movies:
        pos.append(fetch(movies.iloc[i[0]]["id"]))
        rec.append((movies.iloc[i[0]]["title"]))
    return rec,pos

if st.button("Recommend"):
    name,poster=recommend(movie)



    col1, col2, col3= st.columns(3)
    col4, col5,col6=st.columns(3)
    col7, col8, col9=st.columns(3)
    col10 ,col11,col12=st.columns(3)
    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])
    with col6:
        st.text(name[5])
        st.image(poster[5])
    with col7:
        st.text(name[6])
        st.image(poster[6])
    with col8:
        st.text(name[7])
        st.image(poster[7])
    with col9:
        st.text(name[8])
        st.image(poster[8])
    with col10:
        st.text(name[9])
        st.image(poster[9])