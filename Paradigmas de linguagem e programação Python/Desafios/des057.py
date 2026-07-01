#Desafio 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
print()
print('-=-'*10)
print('Registrando o Sexo da Pessoa')
print('-=-'*10)
print()


sexo = str(input('Digite o Sexo [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados incorretos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))



