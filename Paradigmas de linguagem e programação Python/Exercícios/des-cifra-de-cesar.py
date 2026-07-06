
def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index(caractere)
    novo_indice = indice_atual + chave
    # tratando indice maior que o tamanho da string - sequencia
    while novo_indice >= len(seq):
        novo_indice = novo_indice - len(seq)
    # tratando indice negativo (chave com valor negativo)
    while novo_indice < 0:
        novo_indice = novo_indice + len(seq)
    return seq[novo_indice]

texto = 'ABCDE'
chave = -4


minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cifra = ''

for caractere in texto:
    if caractere in minusculas:
        caractere_cifra = cifrar_caractere(caractere, minusculas, chave)
    elif caractere in maiusculas:
        caractere_cifra = cifrar_caractere(caractere, maiusculas, chave)
    else: 
        caractere_cifra = caractere
    cifra += caractere_cifra       

print(cifra)

