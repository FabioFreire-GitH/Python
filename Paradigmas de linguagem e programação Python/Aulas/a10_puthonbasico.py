# Aula 10 - Condições
#if codição():
#   bloco True
#else:
#   bloco False
#Fim
#Importante - Precisa de identação - A tabulaçao - Difeernte do C qu usa {}

#####
# Simplificada
# bloco true if(codiçao) else bloco False
# Fim

nome = str(input('Qual seu nome? '))
if nome == 'Fabio':
    print ('Que nome Lindo você tem!') # Sem o else é condição simples
print ('Bom dia, {}!'.format(nome))

idade = int(input('Qual sua idade? '))
if idade <=30:
    print('Está novo ainda!')
else:
    print('Não está tão novo assim!') 
print('Você tem {} anos.'.format(idade))
print()
n1 = float(input('\nEntre com a primeira Nota: '))
n2 = float(input('Entre com a segunda Nota: '))
media = (n1+n2)/2
print('\nA média do aluno é {}!'.format(media)) 
print()
if media >= 6.0:         #Forma Simplificada -> print('Aprovado!' if media >= 6.0 else 'Reprovado!')
    print('Aprovado!')
else:
    print('Reprovado!')
print()

# Aula 11 - Cores no terminal (Pulei)

# Aula 12 - Condicoes aninhadas 
#if
#elif (o mesmo que else if)
#else


