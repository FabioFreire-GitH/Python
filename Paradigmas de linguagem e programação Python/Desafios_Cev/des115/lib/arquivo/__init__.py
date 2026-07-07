import os
from lib.interface import *

def arquivoExiste(nome):
    pasta = os.path.dirname(__file__)# pasta onde este módulo está
    caminho = os.path.join(pasta, nome)
    try:
        a = open(caminho, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    pasta = os.path.dirname(__file__)# pasta onde este módulo está
    caminho = os.path.join(pasta, nome)
    try:
        a = open(caminho, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criando com sucesso!')


def lerArquivo(nome):
    pasta = os.path.dirname(__file__)# pasta onde este módulo está
    caminho = os.path.join(pasta, nome)
    try:
        a = open(caminho, 'rt')
    except:
        print('Erro ao ler aquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()    

        
def cadastrar(arq, nome='desconhecido', idade=0):
    pasta = os.path.dirname(__file__)
    caminho = os.path.join(pasta, arq)
    try:
        a = open(caminho, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hor de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
        finally:
            a.close()


