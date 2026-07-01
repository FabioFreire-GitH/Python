#DESAFIO 019: Crie a classe Livro, que vai simular a passagem de paginas de um livro, considere também se o usuário chegou ao fim da leitura.
from rich.traceback import install
install()

class Livro:
  
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.tam_livro = paginas
        self.pag_atual = 1

        print(f"Você abriu o livro {self.titulo}, que tem {self.tam_livro} páginas.\nVocê esta na pagina {self.pag_atual}")

    def avancar_paginas(self, avance=1):
        if avance <= 0:
                return print(f"Você permanece na página {self.pag_atual}, avance algumas paginas.")
        else:
            for p in range(self.pag_atual,self.pag_atual+avance):
                if self.pag_atual < self.tam_livro:
                    self.pag_atual += 1
                    print(f"Pág{self.pag_atual}----{p}")


l1 = Livro("O Senhor do Anéis", 30)
l1.avancar_paginas()
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)

l2 = Livro("O Hobbit", 10)
l2.avancar_paginas(0)
l2.avancar_paginas(1)
l2.avancar_paginas(100)
