notas = []
contador = 1
for x in range(2):
    aluno = input('RA: ')
    nota = float(input('Nota: '))
    exibir = [aluno, nota]
    notas.append(exibir)

while contador <= 1:
    aluno = input('RA: ')
    nota = float(input('Nota: '))
    exibir = [aluno, nota]
    notas.append(exibir)

    contador = contador + 1

print('A quantidade de notas foi de:.. ', len(notas))

for n in notas:
    aluno = n[0]
    nota = n[1]
    print("O RA", aluno, "Tirou", nota)