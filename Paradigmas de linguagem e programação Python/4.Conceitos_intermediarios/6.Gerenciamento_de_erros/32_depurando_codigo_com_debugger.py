nomes = ['José', 'Bernardo', 'Paola', 'Fernando', 'Rita']
#idades = [20, 16, 18, 40, 12]
idades = [18, 16, 18, 40, 12]

for nome, idade in zip(nomes, idades):
    if idade > 18:
        maior_de_idade = True
    elif idade < 18:
        maior_de_idade = False
    print(f'{nome} tem {idade} anos. É maior de idade? {maior_de_idade}')