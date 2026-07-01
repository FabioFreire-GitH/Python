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
from transporte import *
from rich import print, inspect
from rich.table import Table

def main():
    dist = 8

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    '''
    entrega = Moto(dist)
    print(f"\nFrete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}")
    
    dist = 80
    entrega = Caminhao(dist)
    print(f"\nFrete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}")
    
    dist = 4
    entrega = Drone(dist)
    print(f"\nFrete de {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}")
    '''
    tabela = Table(title="TABELA DE PREÇOS")

    tabela.add_column("Distancia")
    tabela.add_column("Tipo")
    tabela.add_column("Preço")

    for item in viagem:
        tabela.add_row(f"{dist} Km",f"{type(item).__name__}", f"{item.calc_frete()}")

    print(tabela)


if __name__ == "__main__":
    main()