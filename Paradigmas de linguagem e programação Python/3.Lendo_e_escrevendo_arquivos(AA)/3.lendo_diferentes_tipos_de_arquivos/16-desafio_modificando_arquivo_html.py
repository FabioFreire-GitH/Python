from pathlib import Path

item_remover = 'Comprar pó de café'

pasta_atual = Path(__file__).parent

with open (pasta_atual / 'desafio_texto' / 'lista_tarefas.html', mode='r', encoding='utf-8' ) as html:
    linhas_html = html.readlines()
#print(linhas_html)

# Criar uma copia do arquivo numa nova lista
nova_linhas_html = []
escreve_linha = True
for i, linha in enumerate(linhas_html):

    if i < len(linhas_html) - 3 and item_remover in linhas_html[i+2]:
        escreve_linha = False
    
    if escreve_linha:
        nova_linhas_html.append(linha)
        print(i, linha)

    if '</li>' in linha:
        escreve_linha = True

with open (pasta_atual / 'desafio_texto' / 'lista_tarefas_atualizada.html', mode='w', encoding='utf-8' ) as html:
    html.writelines(nova_linhas_html)    