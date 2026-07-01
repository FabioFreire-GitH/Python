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
class Termostato:
    
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if 16 <= valor <= 30:
            if valor % 0.5 == 0: # posso usar um raise ValueError para tratar um erro e imprimir a mensagem -> solução Guanabara
                self.__temperatura = valor
            else:
                self.__temperatura = round(valor)   
        elif valor < 16:
                self.__temperatura = 16
        elif valor > 30:
                self.__temperatura = 30
               

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}{chr(176)}C"
         



        