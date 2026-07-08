#Aula 13 - Estruturas de Repetição (Iteração) - for 

# Em "português"
# laço c no intervalo(1,10)
#   dentro do laço
# fora do laço

# Em Python exemplos
# for c in range(1,10): # Nao considera o ultimo numero
#   dentro do laço
# fora do laço

# for c in range(0,3):
#   comando 1
#   comando 2
# comando fora do laço

# for c in range(0,3):
#   if condicao
#       bloco_if
#   comando_for 1
#   comando_for 2
# comando fora do laço

# Prática (Conceitos de repetição)

for c in range(1,6):
    print('Oi')
print('Fim')
print()

for c in range(0,6):
    print('Oi')
    print('Fim')
print()

for c in range(1,6):
    print(c)
print('Fim')
print()

for c in range(6, 0, -1):
    print(c)
print('Fim')
print()

for c in range(0, 7, 2):
    print(c)
print('Fim')
print()

n = int(input('Digite um número: '))
for c in range(0, n+1): # o +1 adicionei para demostrar pois quero que incluo o numero digitado
    print(c)
print('FIM')
print()

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p ):
    print(c)
print('FIM')
print()

for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('Fim')
print()

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somátorio de todos os valores foi {}'.format(s))
print()
