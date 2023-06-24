<h1 align="center"> Movie Recommendation System </h1>
<br>

<div align="center">
  
  This is an ML project that uses KNN (K nearest neighbors) [k = 4] algorithm to recommend movies to a user based on features such as ratings, cast, crew, etc. It uses NLP methods to make the text data ready for the model.
  
</div>
<br><br><br>



## 👨‍💻 Techstack
- Flask
- Javascript
- HTML
- Tailwind
- Python

[![My Skills](https://skillicons.dev/icons?i=flask,html,tailwind,javascript,python&perline=6)](https://skillicons.dev)


<br><br><br>

## 💻 Code setup

### Clone the code repository
```
git clone https://github.com/RushabhM03/Movie_Recommendation.git
```


### Create a virtual environment
#### Run the commands from the base folder
```
python -m venv env_name
env_name/scripts/activate (for Windows)
pip install -r requirements.txt
```

### Modify the API keys in the environment variable file (.env) After this run the following commands from the base folder
```
POSTER_IMAGE_PATH="https://image.tmdb.org/t/p/w500/"
SECRET_KEY=" mention any secret key "
GOOGLE_CLIENT_ID="your client id"
MAIL_PORT=465
MAIL_SERVER="smtp.gmail.com"
MAIL_USERNAME=" your email"
MAIL_PASSWORD=" your password "
NEWS_API_KEY=" your news API Key "
```

### Create a client_secret.json file and alter it according to your google account
```
{
    "web":{
        "client_id":"your project URL",
        "auth_uri":"https://accounts.google.com/o/oauth2/auth",
        "token_uri":"https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"your secret key",
        "redirect_uris":["http://127.0.0.1:5000/callback"]
    }
}
```

### Setup Flask app
```
python app.py
```

<br><br><br>

## 🚀Features
1. Google account authentication
2. Movie recommendation
3. View the Training data set
4. Get Real-time entertainment news
5. Working feedback Mail system 
6. UI: Light and dark mode config


<br><br><br>


## 👩‍💻Contributors

Team members

- [**R**ushabh Maru](https://github.com/RushabhM03) - rushabh.maru123@gmail.com
