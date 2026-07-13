#O operador piso
#Usado para obter a parte inteira de uma divisão:
print(9 // 3) # Número 3 cabe 3 vezes no 9, sem resto
# output: 3
print(10 // 3) # Número 3 cabe 3 vezes no 10, resta 1
# output: 3
print(14 // 3) # Número 3 cabe 4 vezes no 14, resta 2
# output: 4
print(15 // 3) # Número 3 cabe 5 vezes no 15, sem resto
# output: 5

#O operador módulo
#Usado para obter a parte restante de uma divisão (de certa forma, é o “complemento” do operador
#piso):
print(9 % 3) # Número 3 cabe 3 vezes no 9, sem resto
# output: 0
print(10 % 3) # Número 3 cabe 3 vezes no 10, resta 1
# output: 1
print(14 % 3) # Número 3 cabe 4 vezes no 14, resta 2
# output: 2
print(15 % 3) # Número 3 cabe 5 vezes no 15, sem resto
# output: 0

#Usos para os operadores de divisão
#Extrair valor de horas, minutos e segundos:
segundos_totais = 65
minutos = segundos_totais // 60
segundos = segundos_totais % 60
print(f'{segundos_totais}s = {minutos}m{segundos}s')
#Descobrir se um número é par:
n = 5
par = (n % 2) == 0
print(f'{n} é par? {par}')
#Descobrir se um número é divisor de outro:
n = 5
div = 3
divisor = (n % div) == 0
print(f'{div} é divisor de {n}? {divisor}')