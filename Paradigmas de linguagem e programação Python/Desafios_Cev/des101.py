#Desafio 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor 
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(valor):
    from datetime import date
    global idade 
    idade = date.today().year - valor
    if idade >=16 and idade < 18 or idade >= 65:
        resp = 'VOTO OPCIONAL.'
    elif idade >= 18 and idade < 65:
        resp = 'VOTO OBRIGATÓRIO.'
    else:
        resp = 'VOTO NEGADO.'
    return resp 
 
    
print()
idade = 0
ano = int(input('Em que anos você nasceu? '))
respvoto = voto(ano)
print(f'Com {idade} anos: {respvoto}')
print()
