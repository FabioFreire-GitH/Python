#Desafio 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = (
    "Lápis", 2.50,
    "Borracha", 1.50,
    "Caderno", 15.90,
    "Estojo", 25.00,
    "Transferidor", 4.20,
    "Compasso", 9.99,
    "Mochila", 120.00,
    "Caneta", 3.00,
    "Livro de Matemática", 55.40,
    "Garrafa Térmica", 45.00,
    "Corretivo", 6.50,
    "Apontador", 2.00,
    "Régua", 5.00,
    "Marca-texto", 4.50,
    "Cola Bastão", 7.00,
    "Tesoura", 8.20,
    "Fichário", 79.90,
    "Folha de Sulfite", 22.00,
    "Pasta Arquivo", 11.50,
    "Calculadora", 35.00
)

print('-'*40)
print('{:^40}'.format('Listagem de Preços'))
print('-'*40)

for pos in range (0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R$ {listagem[pos]:>7.2f}')
print('-'*40)
print()

    
