from time import sleep

class Livro:

    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f"\nVocê abriu o livro '{self.titulo}', que tem {self.total_paginas} páginas.\nVocê esta na pagina {self.pagina_atual}")
        
    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f" Pag{self.pagina_atual} ->", end='', flush=True)
                sleep(0.3)
                cont += 1
        print(f" Você avançou {cont} paginas e agora está na pagina {self.pagina_atual}")
        if self.fim_do_livro():
            print(f"Você chegou ao fim do livro '{self.titulo}'")

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False


l1 = Livro("O Senhor do Anéis", 20)
#l1.avancar_paginas()
l1.avancar_paginas(5)
#l1.avancar_paginas(10)
l1.avancar_paginas(100)

l2 = Livro("O Hobbit", 10)
l2.avancar_paginas(0)