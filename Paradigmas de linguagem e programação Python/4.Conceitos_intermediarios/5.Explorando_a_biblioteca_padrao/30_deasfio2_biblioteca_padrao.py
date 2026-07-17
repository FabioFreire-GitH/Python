#Desafio 02
#Crie uma função chamada diff_tempo, que aceita dois strings no formato HH:MM:SS e retorna a
#diferença de tempo entre eles em um string de mesmo formato.
#Exemplo de uso:
from datetime import datetime
'''
def diff_tempo(inicio, fim):
    formato = '%H:%M:%S'
    hora_inicio = datetime.strptime(inicio, formato)
    hora_fim = datetime.strptime(fim, formato)
    delta = hora_fim - hora_inicio
    return str(delta)
#'''
# ou 
#'''
def diff_tempo(inicio, fim):
    formato = '%H:%M:%S'
    hora_inicio = datetime.strptime(inicio, formato)
    hora_fim = datetime.strptime(fim, formato)
    delta = hora_fim - hora_inicio
    dela_segundos = delta.total_seconds()
    h = dela_segundos // 3600
    m = (dela_segundos % 3600) // 60
    s = dela_segundos % 60
    return f'{int(h)}:{int(m)}:{int(s)}'

#'''
    

inicio = '08:34:21'
fim = '13:55:09'

diff = diff_tempo(inicio, fim)
print(diff)
# output:
# 5:20:48