"""
initializing the flask app
"""

from flask import Flask, render_template
from EasyFlaskRecaptcha import ReCaptcha
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_login import LoginManager
from flask_basicauth import BasicAuth


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    recaptcha = ReCaptcha(app)

    app.config['BASIC_AUTH_USERNAME'] = 'percy_magom'
    app.config['BASIC_AUTH_PASSWORD'] = '6e9ffaebace7cb744324c0e8784a2c69'

    basic_auth = BasicAuth(app)

    from .views import views
    from .auth import auth

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
    app.config.update(dict(
    GOOGLE_RECAPTCHA_ENABLED=True,
    GOOGLE_RECAPTCHA_SITE_KEY="6LdsZ5opAAAAAHQUPPtHtrjHl_TCe9acD5VLI6O6",
    GOOGLE_RECAPTCHA_SECRET_KEY="6LdsZ5opAAAAAOr4Rf2gI8yqtQE6TbPtu6ykwUDs",
    GOOGLE_RECAPTCHA_THEME = "red",
    GOOGLE_RECAPTCHA_TYPE = "image",
    GOOGLE_RECAPTCHA_SIZE = "normal",
    GOOGLE_RECAPTCHA_LANGUAGE = "en",
    GOOGLE_RECAPTCHA_RTABINDEX = 10,
    ))
    recaptcha.init_app(app)
    api = Api(app)
    db.init_app(app)

    @app.route("/submit", methods=["POST"])
    def submit():
        if recaptcha.verify():
            print("SUCCESS")    
        else:
            print("FAILED")

    class Item(db.Model):
        questionId = db.Column(db.Integer, primary_key=True)
        text = db.Column(db.String(100))
        options = db.Column(db.String(100))
        correctAnswer = db.Column(db.Integer)

    class ItemResource(Resource):
        @basic_auth.required
        def get(self, item_id):
            item = Item.query.get(item_id)
            if item:
                return {'questionId': item.questionId, 'text': item.text, 'options': item.options, 'correct_answer': item.correctAnswer}
            return {'message': 'Quiz not found'}, 404

        @basic_auth.required
        def put(self, item_id):
            parser = reqparse.RequestParser()
            parser.add_argument('text')
            parser.add_argument('options')
            parser.add_argument('correctAnswer')
            args = parser.parse_args()

            item = Item.query.get(item_id)
            if item:
                item.text = args['text']
                item.options = args['options']
                item.correctAnswer = args['correctAnswer']
            else:
                item = Item(questionId=item_id, text=args['text'], options=args['options'], correctAnswer=args['correctAnswer'])
                db.session.add(item)

            db.session.commit()
            return {'questionId': item.questionId, 'text': item.text, 'options': item.options, 'correct_answer': item.correctAnswer}, 201

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
