#Desafio 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro válido.')
            continue
        else:
            return n



def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número real válido.')
            continue
        else:
            return n


print()
i = leiaInt('Digite um número Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print()
print(f'Você digitou o número inteiro "{i}" e o número real "{r}".')
print()
