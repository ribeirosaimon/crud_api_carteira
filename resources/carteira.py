from flask_restful import Resource, reqparse
from models.acao import CarteiraModel
from models.usuario import UsuarioModel


class Carteira(Resource):
    def get(self):
        return {'carteira':[acao.json() for acao in CarteiraModel.query.all()]}



class Acao(Resource):
    args = reqparse.RequestParser()
    args.add_argument('acao', type=str, required=True, help="The Field 'acao' cannot be left blank")
    args.add_argument('preco_medio', type=float, required=True)
    args.add_argument('stop_loss', type=float)
    args.add_argument('stop_gain', type=float)
    args.add_argument('usuario',type=int, required=True, help='User not found')


    def get(self, acao_id):
        acao = CarteiraModel.find_acao(acao_id)
        if acao:
            return acao.json()
        return {'message':'Stock not found.'}, 404

    def post(self, acao_id):
        if CarteiraModel.find_acao(acao_id):
            return {'message': f"Stock id '{acao_id}' already exists."}, 400
        dados = Acao.args.parse_args()
        acao = CarteiraModel(acao_id, **dados)
        if not UsuarioModel.find_usuario(dados['usuario']):
            return {'message':'Stock not associated'}, 400
        try:
            acao.save_acao()
        except:
            return {'message': 'An internal error ocurred trying to save stock.'},500
        return acao.json(), 200

    def put(self, acao_id):
        dados = Acao.args.parse_args()
        acao = CarteiraModel(acao_id, **dados)

        acao_encontrada = CarteiraModel.find_acao(acao_id)
        if acao_encontrada:
            acao_encontrada.update_acao(**dados)
            acao_encontrada.save_acao()
            return acao_encontrada.json(), 200
        acao = CarteiraModel(acao_id, **dados)
        acao.save_acao()
        return acao.json(), 201

    def delete(self, acao_id):
        acao = CarteiraModel.find_acao(acao_id)
        if acao:
            try:
                acao.delete_acao()
            except:
                return {'message':'An internal error ocurred trying to delete stock.'}
            return {'message':'Stock deleted.'}
        return {'message':'Stock not found.'}
