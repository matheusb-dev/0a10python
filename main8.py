nome = []
horasTrabalhadas = float(input('Digite o valor da hora trabalhada:... '))
INSS = float(input('Digite o valor do INSS:... '))
print('-------------------------')


for n in range(4):
    name = input("Digite o nome do/a funcionario/a:.. ")
    diasTrabalhados = float(input("Digite quantos dias a pessoa trabalhou: "))
    print('-------------------------')
    exibirNaTela = [name, diasTrabalhados]
    nome.append(exibirNaTela)
    
print('-------------------------')

for n in nome:
    name = n[0]
    diasTrabalhados = n[1]
    print('O funcionario/a: ', name, ', recebe: ', (diasTrabalhados * horasTrabalhadas) * 8)
