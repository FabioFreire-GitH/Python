#DESAFIO 28: Implementando um TERMOSTATO orientado a objetos.
# min 16°C
# max 30°C
# ao ligar -> Liga em 24°C
# incremento e decremento de 0.5°C a gada "girada"
'''
----------------   
   Termostato
----------------     
- __temperatura
+ @temperatura
+ @ftemperatura    
================    
'''
from temperatura import *
from rich import inspect, print

def main ():
    t = Termostato()
  
    try: 
        t.temperatura = 29
    except Exception as e:
        print(f"Houve um problema: {e}")
    except (TypeError, SyntaxError, ValueError):
        t.temperatura = 24
    else:
        print(f"A temperatura atual é de {t.ftemperatura}")
    
       
    inspect(t, private=True, methods= True)

if __name__ == "__main__":
    main()
