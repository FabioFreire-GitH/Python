from abc import ABC, abstractmethod #Abstract Base Classes

class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma ):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def fazer_matricula(self):
        print(f"O aluno {self.nome} fez a matricula!")
    
    def estudar(self):
        print(f"O aluno {self.nome} esta estudando {self.curso} na turma {self.turma}!")


class Professor(Pessoa):
    def __init__(self, nome, idade, espec, nivel):
        super().__init__(nome, idade)
        self.especialidade = espec
        self.nivel = nivel

    def dar_aula(self):
        print(f"O Prof. {self.nome} está dando aula!")

    def estudar(self):
        print(f"O Prof. {self.nome} é especialista em {self.especialidade} no {self.nivel}")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"A funcionária {self.nome} bateu o ponto!")

    def estudar(self):
        print(f"A funcionária {self.nome} se especiaza para a área de {self.setor}.")

