#Desafio 01
#Crie uma função que retorna se um número inteiro n (maior que zero) é primo.
#Dica: um número primo é um número que só é divisível por 1 ou por ele mesmo.

def primo(valor):
    if valor <= 2:
        return True
    for divisor in range(2, valor):
        if valor % divisor == 0:
            return False
    return True

for n in [1,5,10,15,17,22,28]:
    print(f'O Número {n} é primo? {primo(n)}')