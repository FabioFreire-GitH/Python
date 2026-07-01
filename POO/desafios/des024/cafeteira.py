# DESAFIO 024: Simule uma cafeteira orientada a objetos
'''
----------------------------------------
        BebidaQuente{abstract}
======================================== sem atributos
        + preparar ()
        + ferver_agua()
        + misturar (){abstract}
        + servir(){abstract}
-------------------------------------------

    ^               ^               ^
    |               |               |
-----------     ------------    -------------
    Cafe            Cha             Leite
===========     ============    =============
+ misturar()    + misturar()    + misturar()
+ servir()      + servir()      + servir()
'''
from abc import ABC, abstractmethod

class Cafeteira(ABC):
    def preparar(self):
        preparo:str = f"\n--- Iniciando o Preparo ---"
        preparo += self.ferver_agua()
        preparo += self.misturar()
        preparo += self.servir()
        preparo += f"\n--- Bebida Pronta ---\n"
        return print(preparo)

    def ferver_agua(self):
        return f"\n1. Fervendo água a 100 graus Celcius."

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(Cafeteira):
    def misturar(self):
        return f"\n2. Passando áqua pressurizada pelo pó de cafe moido."
    
    def servir(self):
        return f"\n3. Servindo em xícara pequena."


class Cha(Cafeteira):
    def misturar(self):
        return f"\n2. Mergulhando o sachê de ervas na água."
 
    def servir(self):
        return f"\n3. Servindo na xícara de porcelana com limão."


class Leite(Cafeteira):
    def misturar(self):
        return f"\n2. Passando o vapor pressurizao pelo bico da leiteira."
    
    def servir(self):
        return f"\n3. Servindo em caneca grande, já com café."