##############################
#ESTRUTURA DE REPETIÇÃO WHILE
##############################

#O While é utilizado quando não se sabe quando chegar ao fim

# Em "português"
# enquanto não (condição)
#   dentro do laço
# fora do laço

# Em Python exemplo
# while not condição:
#   dentro do laço
# fora do laço

'''
for c in range(1,10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c +=1
print('Fim')
'''
'''
for c in range (1,5):
    n = int(input('Digite um valor: '))
print('Fim')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print ('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1 
print ('Voce digitou {} numeros pares e {} numeros impares.'.format(par, impar))


# Aula 15 foi sobre Break