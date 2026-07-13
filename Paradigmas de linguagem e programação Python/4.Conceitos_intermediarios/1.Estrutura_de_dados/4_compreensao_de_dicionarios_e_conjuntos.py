valores = list(range(10))
print(valores)
# para transformar em um compreensão de conjuntos, basta trocar as [] por {}
maiores_que_cinco = {valor for valor in valores if valor > 5}
print(maiores_que_cinco)
print()
# para dicionario
maiores_que_cinco = {valor:valor+2 for valor in valores if valor > 5}
print(maiores_que_cinco)
# melhor exemplo
valores_em_dolares = {
    'leite' : 0.78,
    'carne' : 4.60,
    'maçã' : 0.35,
}
fator_conversão = 5.31
valores_em_real = {
    chave : round(valor * fator_conversão, 2)
    for chave, valor in valores_em_dolares.items()
}
print(valores_em_real)