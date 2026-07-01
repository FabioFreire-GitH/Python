#DESAFIO 020: Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie um meotodo que permita mostrar a ficha desse gamer.
from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self, jogo):
        self.jogos.append(jogo)
        self.jogos = sorted(self.jogos, key = str.lower)

    def __str__(self):
        return f"{self.nome} -- {self.nick} -- {self.jogos}"
    
    def ficha(self):
        conteudo = f"Nome real: [bold red on white] {self.nome} [/]"
        conteudo += f"\nJogos favoritos:"
        for i in self.jogos:
            conteudo += f"\n:joystick: [blue]{i}[/]"
        cartao = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        return print(cartao)

        

j1 = Gamer("Fabio Freire","RingoStarr")
j1.add_favoritos("Skyrim")
j1.add_favoritos("Assassin's Creed")
print(j1)
j1.ficha()