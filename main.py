# import sys
# sys.path.insert(1, '/home/runner/Deploy/web')
# from flask import Flask
# from views import views

# app = Flask(__name__)
# app.config['SECRECT_KEY'] = 'jsodhsbosjdbsjsjsjsbd'

# app.register_blueprint(views, url_prefix='/')
from web import app

if __name__ == '__main__':
    app.run(host='0.0.0.0')