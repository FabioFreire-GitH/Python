#DESAFIO 29: Simule um diario secreto orientado a objetos.
'''
----------------   
    Diario
----------------     
- __segredos[]
- __senha
----------------
+ escrever(msg)
+ ler (msg)
----------------    
'''
from diario import *
from rich import inspect, print

def main():
    d = Diario()

    d.escrever("Primeira Mensagem!")
    d.escrever("Segunda Mensagem!")
    d.escrever("Terceira Mensagem!")

     # Testando chamada SEM senha (vai cair no TypeError)
    try:
        print(d.ler()) 
    except TypeError as e:
        print(f"[bold red]Erro de validação:[/bold red] {e}")

    # Testando chamada com senha INCORRETA (vai cair no ValueError)
    try:
        print(d.ler("senha_errada"))
    except ValueError as e:
        print(f"[bold red]Erro de acesso:[/bold red] {e}")

    # Testando chamada com senha CORRETA (vai funcionar)
    try:
        print(f"[bold green]{d.ler('1234')}[/bold green]")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    inspect(d, private=True, methods=True)

if __name__ == "__main__":
    main()