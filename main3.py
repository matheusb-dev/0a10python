nome = input("Digite seu nome:.. ");
faltas = int(input('Digite as suas quantidades de faltas:... '))

n1 = float(input('Digite sua 1 nota: '))
n2 = float(input('Digite sua 2 nota: '))
n3 = float(input('Digite sua 3 nota: '))

media = (n1 + n2 + n3)/3
CalMedia = (100 - faltas)/100

if media >= 6 and CalMedia >= 0.75:
    print('sua média foi de', media)
else:
    print('Você reprovou')

print(type(nome))
print(type(n1))
print(type(media))