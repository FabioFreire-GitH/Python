
op = 1

# Versão com if/elif/else
if op == 1:
    print('Opção 1')
elif op == 2:
    print('Opção 2')
else:
    print('Opção inválida!')

# Versão com match case
match op:
    case 1:
        print('Opção 1')
    case 2:
        print('Opção 2')
    case _:
        print('Opção inválida!')

print()
notas = {
'João': 10,
'Maria': 9,
'Mateus': 9.2,
}
match notas:
    case {'Lucas': _} | {'Marcos': _}:
        print('Lucas ou Marcos estão no dicionário!')
    case {'João': 10, 'Maria': 10}:
        print('João e Maria estão no dicionário, e ambos tiraram 10!')
    case {'João': 10, 'Maria': _}:
        print('João e Maria estão no dicionário, e só João tirou 10!')
    case _:
        print('Nenhuma informação encontrada!')