#Desafio  099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def entrada():
    dados = list()
    print('-='*30)
    while True:
        v = input('Digite um número (vazio PARA SAIR): ')
        if v == '':
            break
        if not v.isnumeric():
            v = input('Digite apenas números: ')
        dados.append(int(v))
    dados = tuple(dados)
    print('-='*30)
    return dados
   


def contador(*num):
    print('Analisando os valores passados...')
    tam =len(num)
    print(f'{tam} númenros foram informados: ', end='')
    while True:
        if tam == 0:
            break
        for v in num:
            print(f'[{v}] ', end='')
        print('ao todo.')
        maior = max(num)
        print(f'O maior valor informado foi {maior}')
        break
    print()
    
#Programa principal
print()
valores = entrada()
contador(*valores)
print()