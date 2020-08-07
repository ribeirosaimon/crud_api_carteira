from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Carteira(Resource):
    def get(self):
        return {'carteira':'minha carteira'}


api.add_resource(Carteira, '/carteira')


if __name__ == '__main__':
    app.run(debug=True)
