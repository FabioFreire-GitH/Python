from random import choice, randint, shuffle

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciar_o_dia()

    def reiniciar_o_dia(self):
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres(self):
       return [i for i in self.porta_halteres.values() if i != None] 

    def listar_espacos(self):
       return [i for i, j in self.porta_halteres.items() if j == None] 

    def pegar_haltere(self, peso):
        valores = list(self.porta_halteres.values())
        #if peso not in valores:
            #return False
        halt_pos = valores.index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]
        self.porta_halteres[key_halt] = None
        return peso

    def devolver_halter(self, pos, peso):
        self.porta_halteres[pos] = peso

    def calcular_caos(self):
        num_caos = sum(
            1 for pos, peso in self.porta_halteres.items()
            if peso is not None and pos != peso
        )
        return f'{num_caos / len(self.porta_halteres) *100:.2f} %'


class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo # 1 - normal | 2 - bagunceiro
        self.academia = academia
        self.peso = None

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = choice(lista_pesos)
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()
        if self.tipo == 1:
            if self.peso in espacos:
                self.academia.devolver_halter(self.peso, self.peso)
            else:
                pos = choice(espacos)
                self.academia.devolver_halter(pos, self.peso)
        if self.tipo == 2:
                pos = choice(espacos)
                self.academia.devolver_halter(pos, self.peso)
        self.peso = None


academia = Academia()

usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]
shuffle(usuarios)

for i in range(10):
    shuffle(usuarios)
    for user in usuarios:
        user.iniciar_treino()
    for user in usuarios:
        user.finalizar_treino()


print(academia.porta_halteres)
print(academia.calcular_caos())