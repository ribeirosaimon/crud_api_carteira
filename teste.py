from datetime import datetime
import requests

def adicionar_acao(id_usuario, acao, preco_medio, stop_loss, stop_gain):
    new_id = str(datetime.now()).replace('-','').replace(':','').replace('.','').replace(' ','')[::-1][:6]
    endpoint = f'http://127.0.0.1:5000/carteira/{new_id}'
    print(endpoint)
    add_acao = {'acao':f'{acao}',
                'preco_medio':f'{preco_medio}',
                'stop_loss':f'{stop_loss}',
                'stop_gain':f'{stop_gain}',
                'usuario':f'{id_usuario}'
                }
    add_acao_carteira = requests.request('POST', endpoint, json=add_acao)
    return add_acao_carteira.json()


def criar_carteira_db(id_telegram):
    endpoint = f'http://127.0.0.1:5000/usuarios/{id_telegram}'
    usuario_id = {'usuario':f'{id_telegram}'}
    resposta_usuario = requests.request('POST', endpoint, json=usuario_id)
    return resposta_usuario.json()













criar_carteira = criar_carteira_db(102030)
retorno = adicionar_acao(102030,'oibr3',1,0.5,2)
print(retorno)
