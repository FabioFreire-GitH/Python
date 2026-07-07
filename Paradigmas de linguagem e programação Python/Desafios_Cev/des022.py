#Desafio 22 - Escreva um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas;
#todas as letras minusculas;
#Quantas letras ao todo(sem considerar espaços);
#Quantas letras tem o primeiro nome.
print()
print('='*30)
print('Exibe Nome')
print('='*30)
print()
nome = str(input('Entre com o seu nome completo: ')).strip()
print('\nAnalisando seu nome...')
print('Nome em Letras Maiúsculas: {}'.format(nome.upper()))
print('Nom em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome possui: {} Letras'.format(len(nome) - nome.count(' ')))
print('\nSeu primeiro nome tem: {} Letras'.format(nome.find(' '))) #Nào conheço a função find

#Abaixo minha Solução
nome_dividido = nome.split()
print()
print(nome_dividido)
print('\nO primeiro nome tem: {} Letras'.format(len(nome_dividido[0])))
print()



