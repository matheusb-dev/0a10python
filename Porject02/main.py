from utilitarios import (
    cadastrar_categoria,
    cadastrar_trasancao,
    saldo_total,
)
#categoria
categoria_receitas = cadastrar_categoria("Receitas")
categoria_contas = cadastrar_categoria("Contas")
categoria_viagens = cadastrar_categoria("Viagens")


#transações
cadastrar_trasancao(
    descricao=" Salário Março/2024 ",
    valor= 1200.0,
    categoria=categoria_receitas
)

cadastrar_trasancao(
    descricao=" Chave ",
    valor= -100.0,
    categoria=categoria_contas
)

cadastrar_trasancao(
    descricao=" Cinema ",
    valor= -50.0,
    categoria=categoria_viagens
)

#saldo total
total = saldo_total()

print("Seu saldo total é:.. ", total)


