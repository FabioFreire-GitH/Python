#Desafio 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação (opcional)

#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def entraNotas():
    notas = list()
    sit = False
    valor = 0
    while True:
        n = input('Digite uma nota (s para sair): ').strip()
        if n in 'Ss':
            break
        try:
            notas.append(float(n))
        except ValueError:
            print('Digite apenas números.')
    while True:
        op = input('Exibe Situação? [S/N] ').strip().upper()
        if op in 'SN':
            break
        print('Digite S ou N')
    if op in 'Ss':
        sit = True
    else:
        sit = False
    
    return notas, sit # antes declarei como tupla e tambem funcionou --> tupla(notas , sit) // porem por * na funcao notas e * na chamada da funçao caso deixe como tupla, pis é um metodo de desempacotamento

def notas(num, show=False):
        notas = dict()
        soma = media = 0
        maior = menor = 0
        for i,c in enumerate(num):
           if i == 0:
               maior = c
               menor = c
           else:
               if c > maior:
                   maior = c
               elif c < menor:
                   menor = c
           soma += c
        media = soma / len(num)
        notas['maior'] = maior
        notas['menor'] = menor
        notas['media'] = media
        if show == True:
            if media >= 7.0:
                notas['situação'] = 'Boa'
            elif media >= 5.0:
                notas['situação'] = 'Razoável'
            else:
                notas['situação'] = 'Ruim'
            print('Exibir situação')
        else:   
            print('Não exibir situação')
        
        print(notas)    
        
lista_notas, situacao = entraNotas()
notas(lista_notas, show=situacao)