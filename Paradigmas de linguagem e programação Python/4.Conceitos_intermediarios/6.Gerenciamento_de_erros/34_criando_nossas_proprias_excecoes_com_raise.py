import math

def calcular_raiz_quadrada(numero):
    if numero < 0:
        raise ValueError(f'Impossível calcular a raiz quadrada de {numero}! Apenas valores positivos são válidos.')
    return math.sqrt(numero)


for n in [4, 2, 1, 0, -1]:
    n_raiz = calcular_raiz_quadrada(n)
    print(f'Raiz quadrada de {n}: {n_raiz}')
# Erro na última iteração:
# ValueError: Impossível calcular a raiz quadrada de -1! Apenas valores positivos são válidos.


###
def validar_dados(dados):
    # Checa se dados são o valor nulo
    if dados is None:
        raise TypeError("Dados não podem ser nulos!")
    
    # Checa se as colunas esperadas existem
    for nome_coluna_esperado in ['Data', 'Valor', 'Total']:
        if nome_coluna_esperado not in dados.columns:
            raise ValueError(f"Coluna {nome_coluna_esperado} é necessária, mas não foi encontrada!")

            # Checa se os dados estão vazios (tabela com colunas mas sem linhas)
    if dados.empty:
        raise ValueError("Não há dados inseridos na tabela!")


#dados = ler_dados()
#validar_dados(dados=dados)
# A partir daqui, garanto que os dados são exatamente como esperamos!

####
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError as e:
        mensagem = f'Impossível dividir {a} por {b}. Divisão por zero!'
        raise ValueError(mensagem) from e
    return resultado

n = 10
for divisor in [4, 2, 1, 0, -1]:
    resultado = dividir(n, divisor)
    print(f'Resultado de divisão de {n} por {divisor}: {resultado}')

# Erro na última iteração:
# ValueError: Impossível dividir 10 por 0. Divisão por zero!