from categorias import Categoria
from transacao import Transacao

LISTA_CATEGORIAS = []
LISTA_TRANSACOES = []


def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)

    LISTA_CATEGORIAS.append(nova_categoria)

    return nova_categoria

def cadastrar_trasancao(descricao, valor, categoria):
    nova_transacao = Transacao(descricao=descricao, valor=valor, categoria=categoria,)


    LISTA_TRANSACOES.append(nova_transacao)

    return nova_transacao

def saldo_total():
    total = 0

    for t in LISTA_TRANSACOES:
        #print(t) #t é o obj, ele pode ser o valor, descrição ou a categoria
        total = total + t.valor

    return total


