from flask_restful import Resource
from models.usuario import UsuarioModel


class Usuarios(Resource):
    def get(self):
        return{'usuario':[carteira.json() for carteira in UsuarioModel.query.all()]}

class Usuario(Resource):
    def get(self, usuario):
        usuario = UsuarioModel.find_usuario(usuario)
        if usuario:
            return usuario.json()
        return {'Message':'User not found'}, 404

    def post(self, usuario):
        if UsuarioModel.find_usuario(usuario):
            return {"Message": "The user '{usuario}' alredy exists"}, 400
        usuario = UsuarioModel(usuario)
        try:
            usuario.save_usuario()
        except:
            return {"Message":"A Internal erro ocurred trying to create a new User"}
        return usuario.json()

    def delete(self, usuario):
        usuario = UsuarioModel.find_usuario(usuario)
        if usuario:
            usuario.delete_usuario()
            return {'Message':'User deleted.'}
        return {'Message':'User not found'}
