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
from cafeteira import *

def main():
    bebida = Cha()
    bebida.preparar()

if __name__ == "__main__":
    main()

