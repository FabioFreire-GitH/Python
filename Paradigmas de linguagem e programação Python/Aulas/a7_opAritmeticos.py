#Operadores Aritméticos
'''
Operadores em ordem de precedencia
1 - ()
2 - ** ->Exponênciação 
3 - * / // % -> O que vier primeiro (lembrete: // é divisão inteira e % resto da divisão)
4 - + -

Operadores como função (perde a ordem de precedencia)
- pow(4,3) -> quatro elevado a tres (expoente)

Raiz quadrada exemplo 81**(1/2)
Raiz cubica 81**(1/3)...

No console do python, faça:
'oi'+'olá'
'oi'*5
'='*20
'''
print()
nome = input('Qual é seu nome? ')#ou nome = str(input('Qual é seu nome? '))
print()
print('Prazer em te conhecer {}!'.format(nome))
print()
print('Prazer em te conhecer {:20}!'.format(nome))
print()
print('Prazer em te conhecer {:>20}!'.format(nome))
print()
print('Prazer em te conhecer {:<20}!'.format(nome))
print()
print('Prazer em te conhecer {:^20}!'.format(nome))
print()
print('Prazer em te conhecer {:=^20}!'.format(nome))
print()
n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))
print('A soma vale {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
print()
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')#end evita pular linha
#print()
print('A divisão inteira {}, o resto {} e a potência é {}.'.format(di, r, e))
print()






