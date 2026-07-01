#DESAFIO 016: Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita ai funcionario se apresentar.
from rich import print
from rich import inspect

class Funcionario:
    #Atributos de classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        #Atributos de instancias
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
            return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa} !" # Nao por self.empresa// Pode usar self.__class__.empresa
        

c1 = Funcionario("Fábio", "TI", "Programador")
#inspect(c1, methods=True)
print(c1.apresentacao()) 

