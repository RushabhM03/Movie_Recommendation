import pickle
import requests
import os
from dotenv import load_dotenv
from flask import session, redirect

load_dotenv()

movies = pickle.load(open('Models/movie_list.pkl', 'rb'))
similarity = pickle.load(open('Models/similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    # print(movie_id)
    data = requests.get(url)
    data = data.json()
    vote_avg = data['vote_average']
    poster_path = data['poster_path']
    full_path = os.getenv('POSTER_IMAGE_PATH') + poster_path
    return full_path, vote_avg

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    recommended_movie_votes = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        full_path, vote_avg = fetch_poster(movie_id)
        recommended_movie_votes.append(vote_avg)
        recommended_movies_poster.append(full_path)
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster, recommended_movie_votes

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            # return abort(401)  # Authorization required
            return redirect("/login_front")
        else:
            return function()

    return wrapper

def get_movies(offset=0, per_page=24):
    posters = []
    movie_list = []
    ratings = []
    for i in range(offset, offset + per_page):
        name = movies['title'].iloc[i]
        movie_list.append(name)
        movie_id = movies['movie_id'].iloc[i]
        full_path, vote_avg = fetch_poster(movie_id)
        ratings.append(vote_avg)
        posters.append(full_path)
    return movie_list, posters, ratings

def getNews():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey={}".format(os.getenv('NEWS_API_KEY'))
    data = requests.get(url)
    data = data.json()
    #print(data)
    return data['articles'], data['totalResults']
