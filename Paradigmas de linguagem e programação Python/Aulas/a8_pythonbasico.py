#Trabalhando com Módulos

'''
Importação de bibliotecas (Exemplo de blibliotecas(do mundo real): comida, bebida e doce)
Para incluir usa: import
Cada import carrega todo o contudo (Exemplo: import bebida)
Para importar um item da biblioteca 
usar from: (from doce import pudim)

Mais exemplos:
biblioteca math (matematica)
import math (importa toda a biblioteca matematica)

funcionalidades da biblioteca math:
ceil - arredonta pra cima
floor - pra baixo
trunc - truncar o numero, elimida virgula
pow - potencia (similar **)
sqrt - raiz quadrada
factorial - Fatorial

Para importa uma funcionalidade:

from math import sqrt (importa somente esse funcionalidade)
se precisar de duas por exemploe:
from math import sqrt, factorial

'''
'''
from math import sqrt
#import math
print()
num = int(input('Digite um número: '))
#raiz = math.sqrt(num) #Sem importar o math quando voce for chamar a funcao math., nao aparecerão as funcionalidades
raiz = sqrt(num) #Caso nao importe toda a biblioteca usando somente o from, atribuir desta forma.
print('\nA raiz de {} é igual a {}.'.format(num, raiz))
print('\nCom a formataçao de casas decimais, a raiz é: {:.2f}!'.format(raiz)) #arredonda as casas decimais
print('\nPodemos usar o ceil para arrendondar para cima\n')
print('A raiz de {} arredondando para cima é {}.'.format(num, math.ceil(raiz)))
print()
'''
# Em python.org, podemos estudar e consultar as bibliboecas em DOCS>LIBERY REFERENCES
# quando aperta ctrl + space, voce acessa toda a biblioteca, funcoes etc
import random 
print()
num = random.random()# Gera um numero alearorio do tipo float entre 0 e 1
print(num)
num = random.randint(1, 10) # Gera um numero inteiro entre 1 e 10
print(num)

#para importar biblioteca que nao estao no PC e sim na comunidade PyPI do python.org
#existe milhares de bibliotecas
# testando biblioteca emoji
#Para instalar uma biblioteca no vs, siga o passo a passo abaixo:
# Abra o seu projeto no VS Code.No menu superior, clique em Terminal > Novo Terminal.
# Digite o seguinte comando e aperte Enter (substitua nome_da_biblioteca pelo nome real, 
# por exemplo, pandas ou requests):
# pip install nome_da_biblioteca










