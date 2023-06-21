import pathlib
from flask import Flask, redirect, request, render_template, session, abort, redirect
import pickle
import requests
import pandas as pd
import os
from google.oauth2 import id_token
from pip._vendor import cachecontrol
import google.auth.transport.requests
from google_auth_oauthlib.flow import Flow
from flask_mail import Mail, Message
from flask_paginate import Pagination, get_page_args
from utils import *
from dotenv import load_dotenv

load_dotenv()

movies = pickle.load(open('Models/movie_list.pkl', 'rb'))
similarity = pickle.load(open('Models/similarity.pkl', 'rb'))


app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

app.config['MAIL_SERVER']= os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
#update it with your gmail
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
#update it with your password
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)

@app.route("/login")
def login():
    # return "hi"
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/login_front")
def login_front():
    mode = session.get('mode', 'dark-mode')
    return render_template("login.html", mode=mode)

@app.route("/")
@login_is_required
def home():
    active="home"
    mode = session.get('mode', 'dark-mode')
    return render_template("index.html", mode=mode, active_tab=active)

@app.route("/about")
def about():
    active="about"
    mode = session.get('mode', 'dark-mode')
    return render_template("about.html",mode=mode, active_tab=active)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    active="contact"
    mode = session.get('mode', 'dark-mode')
    if request.method == 'POST':
        try:
            if request.form:
                name = request.form['name']
                rec = request.form['email']
                body = "Sending a copy of your mail to you as well. Hi " + name+". message = " + request.form['message']
                msg = Message('Hello', sender ='rushabh.maru123@gmail.com', recipients = [rec, 'rushabh.maru03@gmail.com'])
                msg.body = body
                mail.send(msg)
                return render_template("sent.html", mode=mode, active_tab=active)
            
        except Exception as e:
            error = {'error': e}
            return render_template("contact.html", mode=mode, active_tab=active)

    else:
        return render_template("contact.html", mode=mode, active_tab=active)

@app.route("/recommendation", methods=['GET', 'POST'])
def recommendation():
    active="recommend"
    mode = session.get('mode', 'dark-mode')
    status = False
    movie_list = movies['title'].values
    if request.method == 'POST':
        try:
            if request.form:
                movies_name = request.form['movies']
                recommended_movies_name, recommended_movies_poster, recommended_movie_votes = recommend(movies_name)
                status = True
                return render_template("recommendation.html", movie_names= recommended_movies_name, poster=recommended_movies_poster, movie_list = movie_list, status = status, votes=recommended_movie_votes, mode=mode, active_tab=active)

        except Exception as e:
            error = {'error': e}
            return render_template("recommendation.html", movie_list = movie_list, status = status, error = error, active_tab=active)
    else:
        print(movie_list)
        return render_template("recommendation.html", movie_list = movie_list, status = status, mode=mode, active_tab=active)

@app.route("/training_set")
def training_set():
    mode = session.get('mode', 'dark-mode')
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    per_page=24
    movie_list, posters, ratings = get_movies(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=100, css_framework='bootstrap5')
    return render_template('training_set.html', movie_list = movie_list, posters = posters, ratings = ratings, page=page, per_page=per_page, pagination=pagination, mode=mode)

@app.route("/news")
def news():
    mode = session.get('mode', 'dark-mode')
    data, len = getNews()
    #print(len)
    return render_template("news.html", data=data, len=len, mode=mode)

@app.route('/toggle-mode')
def toggle_mode():
    if session.get('mode') == 'dark-mode':
        session['mode'] = 'light-mode'
    else:
        session['mode'] = 'dark-mode'
    return redirect(request.referrer)

@app.errorhandler(404)
def page_not_found(error):
    mode = session.get('mode', 'dark-mode')
    return render_template('404.html', mode=mode), 404

@app.errorhandler(401)
def page_restricted(error):
    return render_template('401.html'), 401

if __name__ == "__main__":
    app.debug = True
    app.run()