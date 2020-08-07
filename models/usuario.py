from banco_de_dados import banco


class UsuarioModel(banco.Model):
    __tablename__ = 'usuario'
    usuario = banco.Column(banco.Integer, primary_key=True)

    def __init__(self,usuario):
        self.usuario = usuario

    def json(self):
        return {
            'usuario':self.usuario,
        }

    @classmethod
    def find_usuario(cls, usuario):
        usuario = cls.query.filter_by(usuario=usuario).first()
        if usuario:
            return usuario
        return None

    def save_usuario(self):
        banco.session.add(self)
        banco.session.commit()

    def delete_usuario(self):
        banco.session.delete(self)
        banco.session.commit()
