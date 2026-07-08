
texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

vogais = {'a':0,'e':0,'i':0,'o':0,'u':0}

 
for l in texto.lower():
    if l == 'a':
        vogais['a'] += 1
    elif l == 'e':
        vogais['e'] += 1
    elif l == 'i':
        vogais['i'] += 1
    elif l == 'o':
        vogais['o'] += 1
    elif l == 'u':
        vogais['u'] += 1

for letra, contador in vogais.items():
    print(f'O texto tem {contador} vogais "{letra}".')