#Desafio 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite apenas numeros inteiros.')
        if ok:
            break
    return valor


num = leiaInt('Digite um numero: ')
print(f'Você digitou {num}')