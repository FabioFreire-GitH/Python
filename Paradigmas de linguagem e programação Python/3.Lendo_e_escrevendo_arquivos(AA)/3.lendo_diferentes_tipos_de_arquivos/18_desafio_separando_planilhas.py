import pandas as pd
from pathlib import Path

pasta_atual = Path(__file__).parent


def separar_planilhas():
    pasta_separada = pasta_atual / 'planilhas' / 'planilhas_separadas'
    pasta_separada.mkdir(parents=True, exist_ok=True)

    tabela_clientes_dict = pd.read_excel(
        pasta_atual / 'planilhas' / 'clientes.xlsx',
        sheet_name=None
    )

    for nome_aba, tabela in tabela_clientes_dict.items():
        tabela.to_excel(pasta_separada / f'{nome_aba}.xlsx', index=False)


def consolidar_planilhas():
    pasta_consolidada = pasta_atual / 'planilhas' / 'planilhas_consolidada'
    pasta_consolidada.mkdir(parents=True, exist_ok=True)

    pasta_separada = pasta_atual / 'planilhas' / 'planilhas_separadas'
    with pd.ExcelWriter(pasta_consolidada / 'clientes.xlsx') as consolidada:
        for arquivo in pasta_separada.glob('*.xlsx'):
            tabela = pd.read_excel(arquivo)
            tabela.to_excel(consolidada, sheet_name=arquivo.stem, index=False)


separar_planilhas()
consolidar_planilhas()

