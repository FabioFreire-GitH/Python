#Desafio 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print()
print('-=-'*10)
print('Progressão Aritmética 3.0 (While)')
print('-=-'*10)
print()
primeiro = int(input('Entre com o primeiro Termo: '))
razao = int(input('Entre com a razão: '))
pos = int(input('Entre com a Posição desejada: '))
termo = primeiro
cont = 1
mais = 0
print('\nPA = ', end =' ')
while pos != 0:
    mais = mais + pos
    while cont <= mais:
        print('{} -> '.format(termo), end = '')
        termo += razao
        cont += 1
    print(' Pausa ')
    pos = int(input('Quantos termos você que mostrar a mais? (0 para sair) ')) 
print('\nSaindo do programa...\n')