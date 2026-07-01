
from random import choice


dicionario = {'cenario1':['Corredor','Sala','Deposito'], 'cenario2':['Cripta','Capela','Altar']}

sorteio = choice(list(dicionario.keys()))

sorteio2 = choice(dicionario[sorteio])



print(sorteio)
print(sorteio2)


