# DESAFIO 027: Crie o sistema de batalha entre personagens de um RPG
'''
-------------------------------------------------
            Personagem{abstract}
-------------------------------------------------
            + nome
            + vida
            + golpes
-------------------------------------------------
            + atacar (alvo, força)
            + receber_dano(dano)
            + curar(){abstract}
-------------------------------------------------

        ^                  ^       
        |                  |       
---------------     ------------------ 
    Guerreiro           Mensalista
===============     ===================
   + curar()            + curar()
---------------     -------------------
'''

from personagens import *

def main():
    p1 = Guerreiro("Pikachu", 500)
    p2 = Mago("Merlin", 300)
    p1.atacar(p2, 100)
    p2.atacar(p1, 150)
    p1.atacar(p2, 100)
    p2.atacar(p1, 150)
    p1.atacar(p2, 100)
    p2.atacar(p1, 150)
    p1.atacar(p2, 100)
    p2.atacar(p1, 150)
    p1.atacar(p2, 100)
    p2.atacar(p1, 150)
    p1.curar()
    p2.curar()

    #inspect(p2, methods=True)

if __name__ == "__main__":
    main()

