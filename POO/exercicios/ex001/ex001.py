# Declaração de Classe
class Aluno:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0


    # Métodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1 # simplificando (self.idade += 1)

    def mensagem(self):
        return f"{self.nome} é Aluno(a) e tem {self.idade} anos de idade."


# Declaração de Objetos
a1 = Aluno()
a1.nome = "Fábio"
a1.idade = 47
#print(a1.mensagem())
a1.aniversario()
print(a1.mensagem())

a2 = Aluno()
a2.nome = "Eduardo"
a2.idade = 19
print(a2.mensagem())


