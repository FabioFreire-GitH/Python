# Desafio 53: Escreva um programa que leia um frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
print()
print('-=-'*6)
print('Palíndromo')
print('-=-'*6)
print()
frase = str(input('Entre com um frase: ')).strip().upper()
frase = frase.replace(' ','')
print('\nVocê Digitou: {}'.format(frase))
frase_rev = frase[::-1]
print('A frase invertida é: {}'.format(frase_rev))
if frase_rev == frase:
    print('\nA frase é um Palíndromo!')
else:
    print('\nA frase NÃO é um Palíndromo!')
print('\nFim...\n')
###################################
# SOLUCAO GUANABARA ABAIXO - MELHOR
###################################
print('-=-'*6)
print('Soluçao Guanabara')
print('-=-'*6)
print('Palíndromo')
print('-=-'*6)
print()
frase = str(input('Entre com um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('\nA frase é um Palíndromo!')
else:
    print('\nA frase NÃO é um palíndromo!')
print('\nFim...\n')