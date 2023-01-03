try:
    from flask import Flask
    from views import views
except Exception as e:
    print(f'error occured: {e}')

app = Flask(__name__)
app.config['SECRECT_KEY'] = 'jsodhsbosjdbsjsjsjsbd'

app.register_blueprint(views, url_prefix='/')

    
if __name__=='__main__':
    app.run(host='0.0.0.0')
