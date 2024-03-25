"""
initializing the flask app
"""

from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_login import LoginManager
from flask_basicauth import BasicAuth


db = SQLAlchemy()
app = Flask(__name__)

def create_app():
    #app = Flask(__name__)

    app.config['BASIC_AUTH_USERNAME'] = '05992ccec183b09f19354ba55014c19b'
    app.config['BASIC_AUTH_PASSWORD'] = '6e9ffaebace7cb744324c0e8784a2c69'

    basic_auth = BasicAuth(app)

    from .views import views
    from .auth import auth
    from .pyth import pyth
    from .javascript import javascript
    from .linux import linux
    from .wordpress import wordpress
    from .devops import devops
    from .php import php

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/client.html'), 404
    
    @app.errorhandler(401)
    def unauthorized(e):
        return render_template('error/unauthorized.html'), 401

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('error/server.html'), 500

    app.config.from_object(Config)
    api = Api(app)
    db.init_app(app)

    class Item(db.Model):
        questionId = db.Column(db.Integer, primary_key=True)
        text = db.Column(db.String(100))
        options = db.Column(db.String(100))
        correct_answer = db.Column(db.Integer)

    class ItemResource(Resource):
        @basic_auth.required
        def get(self, item_id):
            item = Item.query.get(item_id)
            if item:
                return {'questionId': item.questionId, 'text': item.text, 'options': item.options, 'correct_answer': item.correct_answer}
            return {'message': 'Quiz not found'}, 404

        @basic_auth.required
        def put(self, item_id):
            parser = reqparse.RequestParser()
            parser.add_argument('text')
            parser.add_argument('options')
            parser.add_argument('correct_answer')
            args = parser.parse_args()

            item = Item.query.get(item_id)
            if item:
                item.text = args['text']
                item.options = args['options']
                item.correct_answer = args['correct_answer']
            else:
                item = Item(questionId=item_id, text=args['text'], options=args['options'], correct_answer=args['correct_answer'])
                db.session.add(item)

            db.session.commit()
            return {'questionId': item.questionId, 'text': item.text, 'options': item.options, 'correct_answer': item.correct_answer}, 201

        @basic_auth.required
        def delete(self, item_id):
            item = Item.query.get(item_id)
            if item:
                db.session.delete(item)
                db.session.commit()
                return {'message': 'Quiz deleted'}
            return {'message': 'Quiz not found'}, 404
    api.add_resource(ItemResource, '/api/v1/<int:item_id>')


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(pyth, url_prefix='/')
    app.register_blueprint(javascript, url_prefix='/')
    app.register_blueprint(linux, url_prefix='/')
    app.register_blueprint(wordpress, url_prefix='/')
    app.register_blueprint(devops, url_prefix='/')
    app.register_blueprint(php, url_prefix='/')

    from .models import User

    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
