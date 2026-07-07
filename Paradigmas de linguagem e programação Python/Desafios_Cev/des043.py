# Desafio 43: Escreva um programa para ler altua e peso e calcular o IMC. mostra o status
# - abaixo 18.5 abaixo do peso
# - entre 18.5 e 25 peso ideal
# - 25 a 30 sobrepeso
# - 30 a 40 obesidde
# - acima de 40 obesidade morbida

print()
print('-=-'*10)
print('Calcularora IMC!')
print('-=-'*10)
print()

peso = float(input('Entre com seu Peso: '))
altura = float(input('Entre com sua altura: '))
imc = peso/altura**2
print()
if imc < 18.5:
    print('Seu IMC é {:.1f}.'.format(imc), end = ' ')
    print('Está Abaixo do Peso!')
elif imc >= 18.5 and imc <= 24.9:
    print('Seu IMC é {:.1f}.'.format(imc), end = ' ')
    print('Está no Peso Ideal!')
elif imc >= 25 and imc <= 29.9:
    print('Seu IMC é {:.1f}.'.format(imc), end = ' ')
    print('Está com Sobrepeso!')
elif imc >=30 and imc <= 39.9:
    print('Seu IMC é {:.1f}.'.format(imc), end = ' ')
    print('Está com Obesidade!')
else:
    print('Seu IMC é {:.1f}.'.format(imc), end = ' ')
    print('Está com Obesidade Morbida!')
print('\nSaindo do Programa...\n')



