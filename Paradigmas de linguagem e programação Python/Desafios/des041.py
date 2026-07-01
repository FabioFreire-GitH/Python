# Desafio 41: Escreva um programa leia o ano de nascimento e informe a categoria (esporte) ate 9 anos mirim; ate 14 infantil; ate 19 junior; ate 20 senior; acima master
from datetime import date
print()
print('-=-'*12)
print('Categorização Esportiva!')
print('-=-'*12)
print()

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('\nAtleta com {} anos --> Categoria Mirim!'.format(idade))
elif idade <= 14:
    print('\nAtleta com {} anos -->Categoria Infantil!'.format(idade))
elif idade <= 19:
    print('\nAtleta com {} anos -->Categoria Junior!'.format(idade))
elif idade <=20:
    print('\nAtleta com {} anos -->Categoria Sênior!'.format(idade))
else:
    print('\nAtleta com {} anos -->Categoria Master!'.format(idade))
print('\nFim de programa...\n')


