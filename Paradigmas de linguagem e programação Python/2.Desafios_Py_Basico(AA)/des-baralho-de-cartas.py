# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:

# gerar_baralho -> retorna um baralho novo. Parâmetros da função
# definem quantas cópias retornar (1 baralho, 2 baralhos, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado
# antes de ser retornado.

# mostrar_baralho -> exibe a quantidade de cartas no baralho e
# mostra quais são.

# dar_as_cartas -> distribui as cartas do baralho entre X
# jogadores, de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de
# cada jogador e mostra quais são.

# A partir dessas funções, o código deve:
# - gerar o baralho e exibi-lo
# - dar as cartas para os jogadores
# - exibir o baralho após as cartas terem sido distribuídas
# - exibir a mão de cada jogador

# DICA: utilize os símbolos ♠ ♥ ♦ ♣ para representar os naipes.
# DICA: utilize a função random.shuffle (módulo random) para embaralhar.
from random import shuffle

naipes = ['♠', '♥', '♦', '♣']
cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def gerar_baralho(qtd = 1, coringa= False, embaralhar = True):
    baralho = []
    
    for _ in range(qtd):
        for naipe in naipes:
            for carta in cartas:
                baralho.append(carta+naipe)
    
    if qtd > 0:
        if coringa:
            qtd *= 2
            for c in range(qtd):
                baralho.append('JK'+f'{c + 1}')

    if embaralhar == True:
        shuffle(baralho)

    return baralho

def mostrar_baralho(baralho):
    total_cartas = len(baralho)
    print(f'Total de {total_cartas} cartas!')
    print(baralho)

def dar_cartas(baralho, qtd_cartas = 5, qtd_jogadores = 2):
    jogadores = {}
    for i in range(qtd_jogadores):
        mao = []
        while len(mao) < qtd_cartas:
            carta = baralho.pop(0)
            mao.append(carta)
        nome_jogador = f"Jogador{i+1}"
        jogadores[nome_jogador] = mao
    return jogadores

def mostrar_jogadores(jogadores):
    for jogador, mao in jogadores.items():
        print(f'Há {len(mao)} cartas na mão do jogador {jogador}')
        print('Cartas:')
        for carta in mao:
            print(f' -> {carta}')



baralho = gerar_baralho(2, True)
mostrar_baralho(baralho)
jogadores = dar_cartas(baralho)
mostrar_jogadores(jogadores)
mostrar_baralho(baralho)


