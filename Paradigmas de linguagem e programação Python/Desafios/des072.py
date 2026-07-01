#Desafio 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
print()
extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oite','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
num = int(input('Digite um valor [0 ate 20]: '))
while True:
    if num >= 0 and num <= 20:
        print(f'\nPor extenso: {extenso[num]}')
        break
    else:
        num = int(input('Numero invalido. Digite um número entre 0 e 20: '))
print('\nFim\n')

