from rich import print
from rich.table import Table


tabela = Table(title="Lista de Preços")

tabela.add_column("Produto", justify="center", style="green")
tabela.add_column("Preço", justify="right")

tabela.add_row("lápis","R$1,50")
tabela.add_row("Borracha","R$5,00",style="blue")
tabela.add_row("Caderno", "[red]R$45,00[/]")

print(tabela)