#Desafio 01
#Converta o loop abaixo para uma compreensão de lista:

valores = [30, 50, 100, 120]
triplos = []

for valor in valores:
    triplo = valor * 3
    triplos.append(triplo)
print(triplos)

#def triplo(valor):
#    return valor * 3

#valores_triplicados = [triplo(valor) for valor in valores]

valores_triplicados = [valor * 3 for valor in valores]
print(valores_triplicados)
