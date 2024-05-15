nome = input("Digite seu nome:.. ");
conceito = 0;

n1 = float(input('Digite sua 1 nota:.. '))
n2 = float(input('Digite sua 2 nota:.. '))
n3 = float(input('Digite sua 3 nota:.. '))

media = (n1 + n2 + n3)/3

print("Sua média foi de:... ", media)

if media<=4:
    conceito = 'D'
elif media<=6:
    conceito = 'C'
elif media<=8:
    conceito = 'B'
else:
    conceito = 'A'

print(nome,", seu conceito foi:.. ", conceito);
