# OS ERROS MAIS COMUNS EM PYTHON
'''
1. IndentationError
    Acontece quando a indentação (o espaço em branco à esquerda) não está correta, seja por ela não
estar consistente, ou não ter sido aplicada corretamente conforme as regras de Python.

• Indentação inconsistente em múltiplas linhas:

x = 1
    y = 2 # IndentationError: unexpected indent

• Indentação faltando em alguma linha que a requer (por exemplo, em for loops):

for valor in [1, 2, 3]:
print(valor) # IndentationError: expected an indented block after 'for' statement on line 1
'''

'''
2. SyntaxError
    Problemas com a sintaxe (regras de escrita) de Python. Algumas das ocorrências mais comuns são:

• Parênteses / aspas / chaves … não fechadas corretamente:

print('olá' # SyntaxError: '(' was never closed
print('olá) # SyntaxError: unterminated string literal (detected at line 1)

• Falta de dois pontos ou parênteses em blocos que necessitam:

for valor in (1, 2, 3) # SyntaxError: expected ':'
    print(valor)
def minha_funcao # SyntaxError: expected '('
    print('Esta é minha função!')

• Uso de caracteres inválidos ou palavras‑chave reservadas como variáveis

meu!valor = 2 # SyntaxError: invalid syntax
for = 2 # SyntaxError: invalid syntax
'''

'''
3. NameError
    Este erro acontece sempre quando você tenta acessar uma variável que não existe:

x = 1
y = 2

print(x)
print(y)
print(z) # NameError: name 'z' is not defined

    Os motivos clássicos para este tipo de erro são:

• Usar uma variável antes de criá-la

• Erro de digitação no nome da variável

• Variável que não foi importada

    Também pode acontecer quando tentamos acessar uma variável fora do seu escopo de criação. No
exemplo abaixo, a variável resultado existe apenas dentro da função. Não temos acesso a ela
mesmo se chamarmos a função:

def minha_funcao():
    resultado = 42


minha_funcao()
print(resultado) # NameError: name 'resultado' is not defined

    Se você se deparar com esta situação, o que você precisa fazer é retornar o valor de dentro da função
para acessá‑lo no escopo global (fora de qualquer função):

def minha_funcao():
    resultado = 42
    return resultado

resultado = minha_funcao()
print(resultado)
'''

'''
4. TypeError
    Este erro ocorre quando o tipo de dado para uma determinada ação está incorreto, como:

• Operações com tipos incompatíveis:

resultado = 10 + '10' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

• Argumentos de tipo incorreto para funções:

resultado = len(10) # TypeError: object of type 'int' has no len()

• Modificar objetos imutáveis:

t = (1, 2, 3)
t[0] = 100 # TypeError: 'tuple' object does not support item assignment

• Tentar fazer indexação de tipos de dado que não suportam esta operação:

n = 100
valor = n[0] # TypeError: 'int' object is not subscriptable

• Tentar “chamar” algo que não é uma função:

n = 100
valor = n() # TypeError: 'int' object is not callable
'''

'''
5. ValueError
    Este erro ocorre quando o tipo de dado está correto, porém seu valor é inválido para uma
determinada ação:

int('10.0.1') # ValueError: invalid literal for int() with base 10: '10.0.1'

seq = [10, 20, 30]
seq.remove(40) # ValueError: list.remove(x): x not in list

'''

'''
6. IndexError
    Este erro ocorre quando o índice passado para alguma sequência vai além dos seus limites:

seq = [10, 20, 30]

print(seq[0])
# output: 10

print(seq[10]) # IndexError: list index out of range
'''

'''
7. KeyError
    Este erro ocorre quando a chave passada para algum dicionário não existe:

dic = {'chave1': 'valor1', 'chave2': 'valor2'}

print(dic['chave1'])
# output: valor1

print(dic['chave10']) # KeyError: 'chave10'

    Além de dicionários, este erro também aparece em outros contextos onde tentamos “pegar” algum
valor com base em um nome (a “chave”). Um dos casos mais comuns é tentando pegar um nome de
coluna que não existe em DataFrames do pandas.
'''

'''
8. AttributeError
    Este erro ocorre quando tentamos acessar um atributo inexistente de algum objeto:

s = 'Python'
print(s.upper())
# output: PYTHON

x = 100
print(x.upper()) # AttributeError: 'int' object has no attribute 'upper'

    Muito comum de acontecer quando um valor pode ser None, e não lidamos com esta possibilidade:

dic = {'chave1': 'valor1', 'chave2': 'valor2'}

for chave in ['chave1', 'chave2', 'chave3']:
    valor = dic.get(chave) # Pode retornar None se a chave não existir!
    print(valor.upper())

    # na última iteração...
    # AttributeError: 'NoneType' object has no attribute 'upper'
'''

'''
9. ImportError
    Este erro ocorre quando tentamos importar um módulo que não é encontrado pelo Python:

import meu_modulo_inexistente
# ModuleNotFoundError: No module named 'meu_modulo_inexistente'

    Em geral, este erro tem duas causas possíveis:

        • Se o módulo que tentamos importar foi baixado externamente (com pip), possivelmente o
        módulo foi instalado em um interpretador de Python, e estamos tentando executar nosso
        código com outro interpretador. Isso pode acontecer quando temos duas ou mais instalações
        de Python em um mesmo computador, ou quando foram criados ambientes virtuais para
        alguma das instalações.

        • Se o módulo foi criado por nós mesmos, então o Python está com dificuldades de encontrar o
        arquivo. Neste caso, é preciso conferir se o nome do arquivo está correto na importação, e em
        que pasta o Python está executando (lembre‑se do os.getcwd()).
'''

'''
10. FileNotFoundError
    Este erro ocorre quando Python tenta abrir algum arquivo que não é encontrado:

with open('arquivo_inexistente.txt') as arquivo:
    print(arquivo.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'arquivo_inexistente.txt'

    Se você encontrar este erro, mas vê que o arquivo existe de fato, então confira os seguintes pontos:

        • Veja se o nome está correto: cuide com letras maiúsculas e minúsculas e confira a extensão
        (dependendo da sua configuração, o explorador de arquivos do Windows pode omitir a
        extensão).

        • Confira se o caminho até o arquivo está correto: cheque a pasta de onde Python está
        executando, printando o valor de os.getcwd, e veja se está fazendo sentido.
'''