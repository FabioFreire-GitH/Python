def meu_filtro(n):
    return n > 2

filtro = filter(meu_filtro, [1,2,3,4])
print(list(filtro))

# Funcao Lambda - funcao anonima
# A funcao acima so existe pois o filter precisa de uma funcao, resolvemos com lambda para nao precisar da funcao

filtro = filter(lambda x: x>2, [1,2,3,4])
print(list(filtro))

#sintaxe: lambda <ARGUMENTOS DA FUNÇÃO>: <LÓGICA DA FUNÇÃO>

print()
lista = ['abc', 1, 4, 6.5, '.', '22']
lista_ordenada = sorted(lista, key=lambda x: len(x) if isinstance(x, str) else x)
print(lista_ordenada)
print()

def ordenamento(x):
    return len(x) if isinstance(x, str) else x

lista = ['abc', 1, 4, 6.5, '.', '22']
lista_ordenada = sorted(lista, key=ordenamento)
print(lista_ordenada)
