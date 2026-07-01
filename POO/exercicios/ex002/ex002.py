# Declaração de Classe
class Aluno:
    """
    Esse classe cria um Aluno, que é uma pessoa que tem nome e idade

    Para criar uma pessoa, use
    variavel = Aluno(nome,idade)
    """
    def __init__(self, nome = "vazio" , idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade


    # Métodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1 # simplificando (self.idade += 1)

    def mensagem(self):
        return f"{self.nome} é Aluno(a) e tem {self.idade} anos de idade."

    def __str__(self): #DUNDER method
        return f"{self.nome} é Aluno(a) e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objetos
a1 = Aluno("Maria", 17)
a1.aniversario()
print(a1.mensagem())
print()

a2 = Aluno("Maria", 17)
a2.aniversario()
print(a2)
print()

print(a1.__doc__)

print(a1.__dict__) #Attribute

print(a1.__getstate__()) # Method 

print(a1.__class__)
