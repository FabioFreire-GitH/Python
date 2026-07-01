# DESAFIO 025: Crie classes capazes de alcular fretes de veiculos diferentes.
'''
-------------------------------------------------
            Transporte{abstract}
-------------------------------------------------
            + distancia
            + frete
-------------------------------------------------
            + calc_frete(){abstract}
-------------------------------------------------

        ^                  ^                ^
        |                  |                |
--------------     ---------------    ----------------
    Moto                Caminhao           Drone
--------------     ---------------    ----------------
+ fator = 0.50      + fator = 1.20     + fator = 9.50
--------------     ---------------    ----------------
+ calc_frete()      + calc_frete()      + calc_frete()

'''
from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)
            
    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R$ {self.frete:.2f}"

class Caminhao(Transporte):
    fator = 1.20

    def __init__(self,distancia):
        super().__init__(distancia)
           
    def calc_frete(self):
        if self.distancia < 50:
            return f"<Distancia menor que 50Km>"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"R$ {self.frete:.2f}"        


class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)
        
    def calc_frete(self):
        if self.distancia > 10:
            return f"<Distancia maior que 10Km>"
        else:
            self.frete = self.distancia * Drone.fator
            return f"R$ {self.frete:.2f}"  