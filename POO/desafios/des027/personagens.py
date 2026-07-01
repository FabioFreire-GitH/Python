# DESAFIO 027: Crie o sistema de batalha entre personagens de um RPG
'''
-------------------------------------------------
            Personagem{abstract}
-------------------------------------------------
            + nome
            + vida
            + golpes
-------------------------------------------------
            + atacar (alvo, força)
            + receber_dano(dano)
            + curar(){abstract}
-------------------------------------------------

        ^                  ^       
        |                  |       
---------------     ------------------ 
    Guerreiro           Mensalista
===============     ===================
   + curar()            + curar()
---------------     -------------------
'''
from abc import ABC, abstractmethod
from rich import print, inspect
from random import randint, choice

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []
    
    def atacar(self, alvo, forca = 50):
        if self.vida > 0 and alvo.vida > 0:
            golpe = choice(self.golpes)
            print(f"O [magenta]{self.nome}({self.vida})[/] atacou [yellow]{alvo.nome}({alvo.vida})[/] com um {golpe}")
            alvo.receber_dano(forca)
            
        else:
            print(f"O ataque [magenta]{self.nome}[/] -> [yellow]{alvo.nome}[/] não pode acontecer!\n")

    def receber_dano(self, dano):
        fator = randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"O [blue]{self.nome}[/] recebeu [red]dano de {fator}[/]\n")

    @abstractmethod
    def curar(self):
        pass

class Guerreiro (Personagem):
    
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco","Golpe de Machado","Pulo Giratório"]

    def curar(self):
        fator = randint (0,100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {fator}[/] de vida.")

class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo","Raio Mortal","Flecha Mágica"]
    
    def curar(self):
        fator = randint (0,100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] conjurou uma magia de cura e [green]recuperou {fator}[/] de vida.")

