from app import app
import os, bottle
from flask import Flask
from flask_ngrok import run_with_ngrok

#app = Flask(__name__)
#run_with_ngrok(app)
if __name__ == '__main__':
    bottle.TEMPLATE_PATH.insert(0, 'app/views/')
    if os.environ.get('APP_LOCATION') == 'heroku':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        app.run(host="localhost", port="8080", debug="True", reloader="True")
