# Desafio 39: Escreva um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade.
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo de alistamento.
# O programa deve mostrar o tempo que falta ou o tempo que passou fora do prazo.
from datetime import date
print()
print('='*30)
print('Alistamento Militar')
print('='*30)
print()

nas = int(input('Entre com seu Ano de Nascimento: '))
hoje = date.today().year
idade = hoje - nas
print('\nQuem nasceu em {} tem {} anos em {}.'.format(nas, idade, hoje))
if idade > 18:
    print('\nVocê deveria ter se alistado há {} anos.'.format(idade-18))
    print('\nSeu alistamento foi em {}'.format(hoje - (idade-18)))
elif idade < 18:
    print ('\nVocê deverá se alistar em {} anos.'.format(18-idade))
    print('\nSeu alistamento será em {}'.format(hoje + (18-idade)))
else:
    print ('\nSeu alistamento é esse ano! {}'.format(hoje))
print('\nFim\n')
