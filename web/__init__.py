from flask import Flask
from .views import views

def create_app():
    app = Flask(__name__)
    app.config['SECRECT_KEY'] = 'jsodhsbosjdbsjsjsjsbd'

    app.register_blueprint(views, url_prefix='/')

    return app
    
create_app()