'''
____________________________
| POLIGONO {abstract}      |
|--------------------------|
| + qtd_lados              |
|--------------------------|
| + perimetro() {abstract} |
| + area() {abstract}      |
|__________________________|

____________________________
|        Quadrado          |
|--------------------------|
| + lado                   |
|--------------------------|
| + perimetro()            |
| + area()                 |
|__________________________|

____________________________
|         Circulo          |
|--------------------------|
| + circulo                |
|--------------------------|
| + perimetro()            |
| + area()                 |
|__________________________|
'''
from abc import ABC, abstractmethod
import math

class Poligono(ABC):
    def __init__(self, lados):
        self.qtd_lados:float = lados

    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.qtd_lados * self.lado

    def area(self):
        return self.lado * self.lado


class Circulo(Poligono):
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio:float = raio

    def perimetro(self):
        return 2 * math.pi * self.raio 

    def area(self):
        return math.pi * self.raio ** 2

