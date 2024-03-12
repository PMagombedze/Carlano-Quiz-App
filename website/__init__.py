"""
initializing the flask app
"""

from flask import Flask, render_template
from flask_socketio import SocketIO

def create_app():
    app = Flask(__name__)
    socketio = SocketIO(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app
