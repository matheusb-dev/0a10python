import os

mensagens = [] #lista vazia

nome = input('Digite seu nome:.. ') #recebe um nome

while True:  #inicia um loop infinito

    os.system('cls')

    if len(mensagens) > 0: #verifica se tem mensagens gravada na lista
        for m in mensagens: #se tiver exibe
                print(m['nome'], "-", m['texto'])

    print('-----------------') #divisao para separar as informações

    # Obtendo o texto
    texto = input("Digite sua mensagem: ") #digite sua mensagem
    if texto == "fim": #verifica se a palavra é fim
        break

    mensagens.append({ #caso contrario adiciona na lista
        'nome': nome,
        'texto': texto
    })