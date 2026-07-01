#DESAFIO 018: Crie a classe Churrasco, onde seja possivel informar quantas pessoas vão participar e mostra quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
from rich import print
from rich.panel import Panel    
from rich.traceback import install
install()

class Churrasco:

    kg_valor:float = 69.80
    consumo_pessoa:float = 0.400
    
    def __init__(self, titulo, qtd=0):
        self.titulo = titulo
        self.participantes = qtd

    def calcular_qtd_carne(self) -> float:
        return Churrasco.consumo_pessoa * self.participantes

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.kg_valor      

    def custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"[bold Green]{self.titulo}[/] com [blue]{self.participantes} participantes[/].\n"
        conteudo += f"Recomendo [blue]comprar {self.calcular_qtd_carne()}Kg[/] de carne\n"
        conteudo += f"O custo total será de [blue]R${self.calcular_custo_total():,.2f}[/]\n"
        conteudo += f"Cada pessoa pagará [red]R${self.custo_individual():,.2f}[/]"
        painel = Panel(conteudo, title=self.titulo, expand=False)

        return print(painel)


c1 = Churrasco('Churras dos Amigos',2)
c1.analisar()

