from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, espec, nivel):
        super().__init__(nome, idade)
        self.especialidade = espec
        self.nivel = nivel

    def dar_aula(self):
        print(f"O Prof. {self.nome} está dando aula!")