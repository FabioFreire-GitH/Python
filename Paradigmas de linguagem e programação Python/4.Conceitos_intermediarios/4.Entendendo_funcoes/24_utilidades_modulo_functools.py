# functools 
from functools import cache

#cache
@cache
def fatorial(n):
    print(f'Valor de n: {n}')
    if n == 1:
        return n
    return n * fatorial(n-1)

fatorial(4)





