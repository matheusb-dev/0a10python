from dataclasses import dataclass

@dataclass
class Aluno:
    name: str #declarei e atribui valores a essas variavel
    ra: str
    years: int

    def mostrar(self):
        print(
            f"Olá, {self.name} seu RA: {self.ra} e vc tem {self.years} anos"
        )

aluno = Aluno(name="Mat", ra="166479", years=18)
aluno.mostrar()