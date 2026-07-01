#DESAFIO 0167 Crie a classe Produto, onde podemos cadastrar nome e preço. Crie também um método mostre uma etiqueta de preço do produto.
from rich import print, inspect
from rich.panel import Panel

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        

    def etiqueta(self):
        linha = '-'*30
        conteudo = f"{self.nome:^30}\n{linha}"
        precofinal = f"R${self.preco:,.2f}"
        conteudo += f"{precofinal.center(30,'.')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
                
        return print(etiqueta)

p1 = Produto("Notebook", 8000.00)
p2 = Produto("Iphone 17 Pro", 12500.00)

p1.etiqueta()
p2.etiqueta()

