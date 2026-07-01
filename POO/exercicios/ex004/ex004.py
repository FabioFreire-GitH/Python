from rich import inspect, print

class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma ):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def fazer_matricula(self):
        print(f"O aluno {self.nome} fez a matricula!")


class Professor(Pessoa):
    def __init__(self, nome, idade, espec, nivel):
        super().__init__(nome, idade)
        self.especialidade = espec
        self.nivel = nivel

    def dar_aula(self):
        print(f"O Prof. {self.nome} está dando aula!")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"A funcionária {self.nome} bateu o ponto!")


#testes
a1 = Aluno("José", 17, "Informática", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1, methods=True)

p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
p1.fazer_aniversario()
p1.dar_aula()
inspect(p1, methods=True)

f1 = Funcionario("Cláudia", 24, "Secretária", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods=True)