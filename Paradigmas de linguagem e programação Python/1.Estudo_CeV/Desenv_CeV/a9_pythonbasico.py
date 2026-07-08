#Manipulando cadeias de Texto
print()
frase = 'Curso em Video Python'
print(frase)
print()
print(frase[9])
print(frase[9:13])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(frase[9:])
print()
print(len(frase)) #funcao importante
print()
print(frase.count('o')) #Conta quantos 'o' tem na variavel frase
print(frase.count('O')) #Conta os 'O' maiusculo (nesse caso: 0)
print(frase.count('o',0,13)) # conta quantos 'o' do indice 0 ate 12
print(frase.find('deo')) #Mostra onde começou no indice, nesse caso o 'd' de 'deo' esta no 11 
print(frase.find('Android')) # quando nao encontra a string na variavel retorna -1
print('Curso' in frase) # outra forma porem retorna booleano 

# Transformação
print()
print(frase.replace('Python','Android')) # Aqui troca(substitui) e imprime, nao troca na variavel.
print(frase.upper()) #metodo tem () no final
print(frase.lower())
print(frase.upper().count('O')) # Aqui transforma tudo em maiusculo para procurar quantos 'O's.
print(frase.capitalize()) #Nao confundir com title
print(frase.title()) # Maiuscula na primeila letra de cada palavra
print()

frase = '   Aprenda Python  '
print(frase)
print(frase.strip()) # Remove todos os espaçoes inuteis no inicio e no fim
print(frase.rstrip()) # Remove somente o lado direito
print(frase.lstrip()) # Esquerda
print()

frase = 'Curso em Vídeo Python'
print(frase.split()) #Divisao no espaço (refaz os indices - nova indexação)(Cada palavra como lista tb indexado de 0 ate a ultima palavra)
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[0][2])
print(dividido[2][3])
print(dividido[3][0:])
print('-'.join(frase)) #poe esse caracter exemplo entre cada letra
print(frase.lower().find('vídeo'))












