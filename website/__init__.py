from flask import Flask
from website.views import views

app = Flask(__name__)

app.config['SECRECT_KEY'] = 'nvbhisuwohsbosqounxhjsbd'

app.register_blueprint(views, url_prefix='/')