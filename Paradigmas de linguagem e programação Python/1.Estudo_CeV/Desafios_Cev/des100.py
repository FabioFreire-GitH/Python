# Desafio100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da 
# lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

def sorteio():
    valores = list()
    cont = 1
    print('Sorteando os valores: ', end='')
    while True:
        num = randint(0, 9)
        if num not in valores:
            valores.append(num)
            print(f'[{num}] ', end='',flush=True)
            sleep(0.7)
            cont += 1
            if cont > 5:
                break
    print()
    return valores

def pares(lista):
    soma = 0
    for v in lista:
        if v %2 == 0:
            soma += v
    print(f'A soma dos valores pares de {lista} é igual a: {soma}\n')

print()
sort = sorteio()
pares(sort)
