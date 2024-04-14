import uuid
import logging
from flask import Flask, request, render_template
from flask_session import Session
from flask_session_captcha import FlaskSessionCaptcha
from pymongo import MongoClient
app = Flask(__name__)

mongo_client = MongoClient("mongodb+srv://paferek553:eJDcia7iLFWl40nC@cluster0.cbqmiqa.mongodb.net/captchadb")

# Captcha Configuration
app.config["SECRET_KEY"] = str(uuid.uuid4())
app.config["CAPTCHA_ENABLE"] = True

# Set 5 as character length in captcha
app.config["CAPTCHA_LENGTH"] = 5

# Set the captcha height and width
app.config["CAPTCHA_WIDTH"] = 160
app.config["CAPTCHA_HEIGHT"] = 60
app.config["SESSION_MONGODB"] = mongo_client
app.config["SESSION_TYPE"] = 'mongodb'
app.config['SESSION_COOKIE_NAME'] = 'session'

# Enable server session
Session(app)

captcha = FlaskSessionCaptcha(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        if captcha.validate():
            return "success"
        else:
            return "fail"
    return render_template('form.html')

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True)


