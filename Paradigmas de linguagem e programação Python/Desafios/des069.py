#Desafio  069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 
print()
print('-='*20)
print('Cadastro de Pessoas')
maior18 = qtdhomem = qtdmulherjovem = 0
op = 'S'
while op in 'Ss':
    print('-='*20)
    nome = str(input('Digite o Nome: ')).strip()
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Digite o Sexo [M/F]: ')).strip().upper()[0]
    print('-='*20)
    if op != 'S' and op != 'N':
        print('\nOpção Invalida !')
    else:
        if idade > 18:
            maior18 += 1
        if sexo == 'M':
            qtdhomem += 1
        if sexo == 'F' and idade < 20:
            qtdmulherjovem += 1
        if op == 'N':
            break
    op = str(input('Deseja Continuar [S/N]?')).strip().upper()[0]
print('-='*20)
print(f'\nForam cadastradas {maior18} pessoa(s) maior(es) de 18 anos.')
print(f'\nForam cadastrados {qtdhomem} homens.')
print(f'\nForam cadastradas {qtdmulherjovem} mulheres com menos de 20 anos.\n')
print('-='*20)
print('\nSaindo do Programa...\n')
