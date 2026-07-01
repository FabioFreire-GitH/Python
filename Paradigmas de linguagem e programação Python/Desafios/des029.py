#Desafio 29 - Escreva um programa que leia a velociade do carro. Se ultrapassar 80km/h - ele diz multado. A multa vai custar R$ 7,00 por cada Km/h acima do limite. 
print()
print('='*35)
print('Verifica Multa de Velocidade')
print('='*35)
print()
vel = float(input('Verificando a velocidade em Km/h do carro, informe a velocidade? '))
if vel > 80:
    print('Multado por excesso de Velocidade. (Limite da Via: 80 Km/h)')
    multa = (vel - 80) * 7
    print('Sua velocidade é {:.2f}, multa prevista R$ {:.2f}.'.format(vel, multa))
#else: ## para condição simples, não precia do else.
#    print('Velocidade Permitida!')
print('Tenha um Bom Dia!')
print('Fim do Programa...')
print()
