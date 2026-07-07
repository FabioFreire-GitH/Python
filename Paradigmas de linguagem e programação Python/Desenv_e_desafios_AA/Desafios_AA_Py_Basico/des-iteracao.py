numeros = [2,5,7,9,6,8,3]
palavras = ['pedra','faca','anzol','dedo','figura']
soma = maior = 0

for n in numeros:
    soma += n
    if n >= maior:
        maior = n

print(numeros)    
print(f'A soma é {soma}')
print(f'A media é {soma/len(numeros):.2f}')
print(f'O maior númnero é: {maior}')
print()

tam = 0
for p in palavras:
    tam = len(p)
    if tam >= 5:
        print(f'({p})', end = ",")
print()






