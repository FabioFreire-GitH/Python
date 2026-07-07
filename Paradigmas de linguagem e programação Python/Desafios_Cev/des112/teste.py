#Desafio 112

from utilidades import moeda
from utilidades import dado

print()
p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 20, 12)
print()


