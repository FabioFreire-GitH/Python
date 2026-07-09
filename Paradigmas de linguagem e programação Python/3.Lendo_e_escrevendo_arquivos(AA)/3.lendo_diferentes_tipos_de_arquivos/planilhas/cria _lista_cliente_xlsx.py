from names import get_full_name
from random import randint

count = 62
nomes = []

for i in range(count):
    nomes += [get_full_name()]
    print(nomes[-1])

for i in range(count):
    print(randint(50000000, 60000000))

for i in range(count):
    print((nomes[i].split()[0] + nomes[i].split()[1][0] + '@email.com'))

for i in range(count):
    print(str(randint(4014, 105000)))