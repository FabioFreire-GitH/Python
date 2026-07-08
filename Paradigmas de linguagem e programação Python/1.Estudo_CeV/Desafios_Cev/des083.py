#Desafio 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
print('-='*30)
print('{:^60}'.format('DESAFIO 83'))
print('-='*30)

expr = str(input('Digite a expressão matematica: '))
pilha = []

for char in expr: # Aqui vai verificar cada caracter na variavel tipo str
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:     
    print('Expressão Correta!')
else:
    print('Expressão Invalida!')
print('\nFim\n')