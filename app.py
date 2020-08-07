from flask import Flask
from flask_restful import Api
from resources.carteira import Carteira, Acao

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()


api.add_resource(Carteira, '/carteira')
api.add_resource(Acao, '/carteira/<int:acao_id>')

if __name__ == '__main__':
    from banco_de_dados import banco
    banco.init_app(app)
    app.run(debug=True)
