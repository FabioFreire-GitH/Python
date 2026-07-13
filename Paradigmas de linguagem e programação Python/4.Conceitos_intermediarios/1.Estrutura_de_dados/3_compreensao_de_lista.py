valores = list(range(10))
print(valores)
maiores_que_cinco = []
for valor in valores:
    if valor > 5:
        maiores_que_cinco.append(valor)
print(maiores_que_cinco)
print()
#sintaxe explicativa
#NOVA_LISTA = [RESULTADO para cada ELEMENTO em SEQUENCIA se CONDIÇÃO]
menores_que_cinco = [valor for valor in valores if valor < 5]
print(menores_que_cinco)
print()
def valor_ao_quadrado(valor):
    return valor ** 2

numeros_pares = [
    valor_ao_quadrado(valor)
    for valor in valores
    if valor % 2 == 0
]
print(numeros_pares)

