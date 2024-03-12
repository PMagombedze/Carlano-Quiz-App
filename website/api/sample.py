from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)
api = Api(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)

with app.app_context():
    db.create_all()

class ItemResource(Resource):
    def get(self, item_id):
        item = Item.query.get(item_id)
        if item:
            return {'id': item.id, 'name': item.name, 'price': item.price}
        return {'message': 'Item not found'}, 404

    def put(self, item_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('price')
        args = parser.parse_args()

        item = Item.query.get(item_id)
        if item:
            item.name = args['name']
            item.price = args['price']
        else:
            item = Item(id=item_id, name=args['name'], price=args['price'])
            db.session.add(item)

        db.session.commit()
        return {'id': item.id, 'name': item.name, 'price': item.price}, 201

    def delete(self, item_id):
        item = Item.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return {'message': 'Item deleted'}
        return {'message': 'Item not found'}, 404

api.add_resource(ItemResource, '/items/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True)