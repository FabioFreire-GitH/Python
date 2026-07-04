
texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

vogais = ('a','e','i','o','u')

 
cont = 0
for _ in texto.lower():
    if _ in vogais:
        cont += 1

print(f'O texto tem {cont} vogais.')