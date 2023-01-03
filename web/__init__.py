from flask import Flask
from .views import views

app = Flask(__name__)

app.config['SECRECT_KEY'] = 'nvbhisuwohsbosqounxhjsbd'

app.register_blueprint(views, url_prefix='/')