#DESAFIO 021: Crie a classe Canete, onde simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa.
from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"    
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def escrever(self, msg):
            if self.tampada:
                print(f":prohibited: A {self.cor}caneta[/] está Tampada!")
            else:
                print(f"{self.cor}{msg}[/]", end=' ')
      
    def pular_linha(self, qtd):
        print('\n'*qtd, end= '')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


c1 = Caneta("Azul")
c2 = Caneta("Vermelha")
c3 = Caneta("verde")

c1.destampar()

c1.escrever("Olá, Mundo!")
c1.pular_linha(2)
c2.escrever("Funciona!")
c3.escrever("Deu Certo!")