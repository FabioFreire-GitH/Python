#desafio 87: Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
print('-='*30)
print('{:^60}'.format('DESAFIO 87'))
print('-='*30)
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somapar =soma3c = 0
maior2l = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if matriz[l][2]:
            soma3c += matriz[l][2]
        if matriz[1][c] > maior2l:
            maior2l = matriz[1][c]
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares foi: {somapar}')
print(f'A soma dos valores da 3ª coluna foi: {soma3c}')
print(f'O maior valor da 2ª linha foi: {maior2l}')
print('\nFim\n')
