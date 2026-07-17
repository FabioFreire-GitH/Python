import locale # posso chamar pelo from tambem
#Configirar 
locale.setlocale(locale.LC_ALL, '')#representa que todas as formatacoers deve ser com a linha que vamos passar(numero, texto, moeda)
x = 12.5
print(locale.str(x))

y = 1279.956456
print(locale.currency(y))
print(locale.currency(y, grouping=True))

# Expressoes Regulares

import re

padrao = '[0-9]'
texto = 'Escri este texto há 8 anos atrás'
print(re.search(padrao, texto))
match = re.search(padrao, texto)
match.group()
print(match.group())
print(match.start(), match.end()) # onde começa e termina o numero encontrado no texto
print()


texto = "O ônibus saiu com 45min de atraso, estava previsto para sair 16h30"

padrao = '[0-9]{2}' # Exatamente 2 dígitos seguidos

match = re.search(padrao, texto)
print(match)
# output: <re.Match object; span=(18, 20), match='45'>

padrao = '[0-9]{2}h' # Match anterior seguido de caratere 'h'
match = re.search(padrao, texto)
print(match)
# output: <re.Match object; span=(61, 64), match='16h'>

padrao = '[0-9]{2}$' # Exatamente 2 dígitos no final da frase
match = re.search(padrao, texto)
print(match)
# output: <re.Match object; span=(64, 66), match='30'>

padrao = 'e.' # Caractere "e" seguido de qualquer caractere
match = re.search(padrao, texto)
print(match)
# output: <re.Match object; span=(35, 37), match='Es'>

padrao = 'e.*' # Caractere "e" seguido de quaisquer caracteres (plural!)
match = re.search(padrao, texto)
print(match)
# output: <re.Match object; span=(35, 66), match='Estava previsto para sair 16h30'>

match = re.findall(padrao, texto)
print(match)
# output: ['45', '16', '30']

print()

texto = """
Nome: Marcos | Idade: 30| CPF: 012.345.678-90 | País de origem: Brasil
Nome: Ana | Idade: 28 |CPF: 098.765.432-10 | País de origem: Brasil
Nome: Isadora | Idade: Não informado | CPF:090.080.070-65 | País de origem: Brasil
Nome: Guilherme| Idade: 21 | CPF: 111.222.333-45| País de origem: Brasil
"""

padrao = '[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}'

print(re.findall(padrao, texto))

