"""
initializing the flask app
"""

from flask import Flask
from EasyFlaskRecaptcha import ReCaptcha
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from .config import Config

def create_app():
    app = Flask(__name__)
    recaptcha = ReCaptcha(app)

    from .views import views
    from .auth import auth

    app.config.from_object(Config)
    app.config.update(dict(
    GOOGLE_RECAPTCHA_ENABLED=True,
    GOOGLE_RECAPTCHA_SITE_KEY="6Lf74pUpXXXXXXXXXXXXXXXi012KXXXX7KB-31XXXH",
    GOOGLE_RECAPTCHA_SECRET_KEY="6LXXXXXXXXXXAFX-ZAXXXXXGSd-y5g0o-JZXXXXB",
    GOOGLE_RECAPTCHA_THEME = "red",
    GOOGLE_RECAPTCHA_TYPE = "image",
    GOOGLE_RECAPTCHA_SIZE = "normal",
    GOOGLE_RECAPTCHA_LANGUAGE = "en",
    GOOGLE_RECAPTCHA_RTABINDEX = 10,
    ))
    recaptcha.init_app(app)
    db = SQLAlchemy(app)
    api = Api(app)

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

    with app.app_context():
        db.create_all()

    class ItemResource(Resource):
        def get(self, item_id):
            item = Item.query.get(item_id)
            if item:
                return {'questionId': item.questionId, 'text': item.text, 'options': item.options, 'correct_answer': item.correctAnswer}
            return {'message': 'Quiz not found'}, 404

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

    return app
