import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path

data_json = """
{
    "assinantes" : [
    {
        "nome": "Carlos Silva",
        "telefone": "11999998888",
        "email": "carlos.silva@email.com",
        "em_dia": true
    },
    {
        "nome": "Ana Souza",
        "telefone": "21988887777",
        "email": "ana.souza@email.com",
        "em_dia": false
    },
    {
        "nome": "Marcos Oliveira",
        "telefone": "31977776666",
        "email": "marcos.oliveira@email.com",
        "em_dia": true
    }
    ],
    "data_extração" : "2023/08/22"
}
"""

# Convertendo json para dicionario
dado_convertido = json.loads(data_json)
''''
print(type(data_json))
print(type(dado_convertido))
print(dado_convertido)
'''
# Convertendo novamente para json
'''
dado_desconvertido = json.dumps(dado_convertido, ensure_ascii=False, indent=2)
print(type(dado_convertido))
print(type(dado_desconvertido))
print(dado_desconvertido)
'''

# Lendo arquivos json
pasta_atual = Path(__file__).parent
with open(pasta_atual / 'jsons' / 'assinantes.json') as f:
    dado_carregado = json.load(f)
print(type(dado_carregado))
print(dado_carregado)


# Escrevendo arquivos json
with open(pasta_atual / 'jsons' / 'assinantes_copia.json', 'w') as f:
    json.dump(dado_carregado, f, indent=2, ensure_ascii=False)

