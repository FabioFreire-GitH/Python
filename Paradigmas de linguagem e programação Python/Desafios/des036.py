#Desafio 36: Escreva um programa para aprovar o emprestimo bancario para compra de casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# - Calcule o valor da prestação mensal, sabendo que lea não pode execede 30 % do salario ou entao o emprestimo será negado. (nao precisa calcular juros)
print()
print('='*30)
print('Credito Imobiliário')
print('='*30)
print()
valor = float(input('Qual o valor do Imovel desejado? R$ '))
sal = float(input('Qual o seu salário mensal? R$ '))
prazo = int(input('Em quantos anos deseja financiar? '))

prazo_total = prazo * 12
prestacao = valor / prazo_total
limite = sal*30/100

if prestacao > limite:
    print('\nAs {} parcelas de R$ {:.2f} do credito imobiliário, excedem os 30%(R$ {:.2f}) do seu salario de R$ {:.2f}'.format(prazo_total, prestacao, limite, sal))
    print('\nCREDITO REPROVADO!')
else:
    print('\nAs {} parcelas de R$ {:.2f} do credito imobiliário, cabem nos 30%(R$ {:.2f}) do seu salario de R$ {:.2f}'.format(prazo_total, prestacao, limite, sal))
    print('\nCREDITO APROVADO!')
print('\nFIM...\n')

