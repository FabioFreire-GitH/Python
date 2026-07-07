# Aula 20 e 21: FUNÇÕES
#Explicaçoes do Guanabara

#Modularização
# Focos:
# - Dividir um programa grande
# - Aumentar a legibilidade
# - Failitar a Manutenção

# Parte Teorica:

import a22_uteis

num = int(input('Digite um Valor: '))
fat = a22_uteis.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O Dobro de {num} é {a22_uteis.dobro(num)}')
print()

#Vantagens
#- Organização do codigo
#- Facilita na manutenção
#- Ocultação de codigo detalhado
#- Reulização em outros Projetos



#Pacotes

#Caso tivermos muitos modulos
#Exemplo igual ao aterior

# Pacotes é a junção de Modulos separados por assuntos (Uma pasta com modulos - Uma pacote)(Pacotes Uteis - dentro podemos terr funcoes que tratam numeros, string, datas, manip de cores ... por exemplo)

# Basta criar de dentro do projeto, uma pasta chamata uteis por exemplo (como o exemplo anterior)
# Podem existir outro pacotes dentro de pacotes (pastas separadas : sub pasta - numeros; strings; datas; cores etc...)

# Sintaxe para nome de arquivos dentro de pacotes: __init__.py, precisa ser criado dentro de cada pasta conforme exemplo acima. (o pycharm ja cria o arquivo caso voce crie um pacote)
# o Arquivo uteis(principal do pacote) tambem pode ter o arquivo __init__.py

from meu_pacote import numeros

num = int(input('Digite um Valor: '))
fat = numeros.fatorial(num)
print(f'O Fatorial de {num} é {fat}')
print(f'O Dobro de {num} é {numeros.dobro(num)}')


    