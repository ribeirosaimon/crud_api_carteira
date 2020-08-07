from banco_de_dados import banco


class CarteiraModel(banco.Model):
    __tablename__ = 'carteira'
    acao_id = banco.Column(banco.Integer, primary_key=True)
    acao = banco.Column(banco.String(15))
    preco_medio = banco.Column(banco.Float(precision=2))
    usuario = banco.Column(banco.Integer, banco.ForeignKey('usuario.usuario'))

    def __init__(self, acao_id, acao, preco_medio, usuario):
        self.acao_id = acao_id
        self.acao = acao
        self.preco_medio = preco_medio
        self.usuario = usuario

    def json(self):
        return {
            'acao_id':self.acao_id,
            'acao':self.acao,
            'preco_medio':self.preco_medio,
            'usuario':self.usuario
        }

    @classmethod
    def find_acao(cls, acao_id):
        acao = cls.query.filter_by(acao_id=acao_id).first()
        if acao:
            return acao
        return None

    def save_acao(self):
        banco.session.add(self)
        banco.session.commit()

    def update_acao(self, acao, preco_medio):
        self.acao = acao
        self.preco_medio = preco_medio

    def delete_acao(self):
        banco.session.delete(self)
        banco.session.commit()
