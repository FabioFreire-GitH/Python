
x = input('Digite algo para testarmos: ')
y = bool(x)
print()
print('Seu tipo é:')
print(type(x))
print()
print('Testaremos o valor digitado, se True para verdadeiro ou False se falso.\n')
print('- Possui alguma informação digitada? {}'.format(y))
print('- Todo conteúdo é do tipo numerico? {}'.format(x.isnumeric()))
print('- Todo conteúdo é do tipo Letra?')
print(x.isalpha())
print('- Todo conteúdo é do tipo Alfanumerio?')
print(x.isalnum())
print('- Todo conteúdo é do tipo Maiuscula?')
print(x.isupper())
print('- Todo conteúdo é do tipo Minuscula?')
print(x.islower())
print('- Possui somente um espaço?')
print(x.isspace())
print()
print('- O conteudo pode ser usado como variável, função ou classe no Python?')
print(x.isidentifier())#Verifica se a string pode ser usada como nome de uma variável, função ou classe no Python
print('- Todo o conteúdo pertence a tabela ascii ?')
print(x.isascii())#Verifica se todos os caracteres da string pertencem à tabela ASCII.
print('- Todo o conteúdo pertence a case 10 (decimal), ou seja todo a strings contem numerios de 0 a 9?')
print(x.isdecimal())#Retorna True apenas se a string contiver números de 0 a 9 (caracteres usados para formar números na base 10).
print('- Todo o conteúdo possui numerios decimais ou caracteres numéricos especiais (numeros sobrescritos(expoentes) ou subscritos)?')
print(x.isdigit())#Retorna True se a string contiver números decimais OU caracteres numéricos especiais, como números sobrescritos (expoentes) e subscritos.
print('- O conteudo possui formato de título? Ou seja, cada palavra deve conter a primeira letra maiuscula.')
print(x.istitle())#O formato de título significa que a primeira letra de cada palavra deve estar em maiúscula e todas as demais letras devem estar em minúsculas.

