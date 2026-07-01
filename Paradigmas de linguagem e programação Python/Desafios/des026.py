#Desafio 26 - Escreva um programa que leia uma frase pelo teclaso e mostre: 
# - Quantas vezes aparece a letra "A";
# - Em que posição ela aparece a primeira vez;
# - Em que posição ela aparece a última vez.
print()
print('='*30)
print('Entronte a Letra "A"')
print('='*30)
print()
frase = str(input('Entre com uma frase: ')).strip().upper()
print('A letra "A", aparece {} vezes!'.format(frase.count('A')))
print('A letra "A" aparece na posição {} pela primeira vez!'.format(frase.find('A') + 1))
print('A letra "A" aparece na posição {} pela última vez!'.format(frase.rfind('A') + 1))
print()

