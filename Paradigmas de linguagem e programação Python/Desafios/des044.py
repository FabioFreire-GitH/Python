# Desafio 44: Escreva um programa que calcule o valor a ser pago por um produto considerando seu preco normal e condicao de pagamento
# - a vista (dinheiro ou pix) 10% de desconto
# - a vista cartao 5% desconto
# - em 2 x cartao preco normal
# - 3 x ou mais 20 % de juros

print()
print('-=-'*8)
print('Formas de Pagamento')
print('-=-'*8)
print()

valor = float(input('Informe o preço do produto: '))

print('''\nEscolha a opção de pagamento:\n
    (1) - À vista (Dinheiro ou PIX) - Desconto 10%
    (2) - À vista (Cartão de Credito) - Desconto 5%
    (3) - Parcelado em até 2x (no Cartão) - Valor Normal
    (4) - Parcelado em 3 ou mais vezes - Acréscimo 20%''')
opcao = int(input('\nEscolha sua opção de pagamento: '))
if opcao == 1:
    novo = valor - valor*10/100
    print('\nO valor à pagar será de R$ {:.2f}'.format(novo))
elif opcao == 2:
    novo = valor - valor*5/100
    print('\nO valor à pagar será de R$ {:.2f}'.format(novo))
elif opcao == 3:
    novo = valor
    print('\nO valor à pagar será de R$ {:.2f}'.format(novo))
elif opcao == 4:
    novo = valor + valor*20/100
    print('\nO valor à pagar será de R$ {:.2f}'.format(novo))
else:
    print('\nOpcao Invalida!')
print('\nSaindo do programa...\n')
