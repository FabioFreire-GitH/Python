# DESAFIO 23: Implemente o seguinte diagrama de clasees: 
from poligono import *
from rich.traceback import install
from rich import print, inspect
install()

def main():
    q1 = Quadrado(12)
    print(f"Perímetro = {q1.perimetro():.1f}")
    print(f"Área = {q1.area():.1f}")
    
    c1 = Quadrado(12)
    print(f"Perímetro = {c1.perimetro():.1f}")
    print(f"Área = {c1.area():.1f}")
    

if __name__ == "__main__":
    main()
