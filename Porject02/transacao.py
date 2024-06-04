from dataclasses import dataclass
from categorias import Categoria #pega o arquivo categoria abre ele e pega a CAtegoria#


@dataclass

class Transacao:
    descricao: str
    valor: float
    categoria: Categoria


    def exibir(self):
        print(
            f"Descrição: {self.descricao} | VALOR: {self.valor} | Categoria: {self.categoria.nome}" #categoria se torna um obj
        )