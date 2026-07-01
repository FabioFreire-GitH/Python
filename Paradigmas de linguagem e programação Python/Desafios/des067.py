#Desafio 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
print()
print('-=-'*5)
print('TABUADA 3.0')
print('-=-'*5)
print()
print('-'*30)
n = int(input('Quer ver a tabuada de qual valor? '))
print('-'*30)
r = 0
cont = 1
while n >= 0:
    if n < 0:
        break
    if cont <= 10:
        print (f'{n} x {cont} = {r}')
        cont += 1
    else: 
        print('-'*30)
        n = int(input('Quer ver a tabuada de qual valor? '))
        print('-'*30)
        cont = 1
print('\nPrograma TABUADA encerrado. Até mais...\n')    
