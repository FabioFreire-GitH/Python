x: int = 10
y: float = 5.5
nome: str = 'Juliano'

nomes: list[str] = ['Luiza', 'Henrique', 'Ricardo']
valores: tuple[int] = (0, 1, 2, 3)
produtos: dict[str, float] = {
'leite': 4.50,
'pão': 1.20,
'carne': 15.90,
}

def somar(a: int, b: int) -> int:
    return a + b

print(somar(1, 2))
# output: 3


def somar(a: int, b: int) -> int:
    return a + b

print(somar(1.5, 2.2))
# output: 3.7

print(somar('Olá', 'Mundo'))
# output: OláMundo

def somar(a: int,b: str,c: list[int],d: tuple,) -> str:
    # Corpo da função aqui
    pass

