brasil = {
    # Norte
    "Acre": "Rio Branco",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Pará": "Belém",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Tocantins": "Palmas",

    # Nordeste
    "Alagoas": "Maceió",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Maranhão": "São Luís",
    "Paraíba": "João Pessoa",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio Grande do Norte": "Natal",
    "Sergipe": "Aracaju",

    # Centro-Oeste
    "Goiás": "Goiânia",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Distrito Federal": "Brasília",

    # Sudeste
    "Espírito Santo": "Vitória",
    "Minas Gerais": "Belo Horizonte",
    "Rio de Janeiro": "Rio de Janeiro",
    "São Paulo": "São Paulo",

    # Sul
    "Paraná": "Curitiba",
    "Rio Grande do Sul": "Porto Alegre",
    "Santa Catarina": "Florianópolis"
}
print()
print('-='*30)
print('{:^60}'.format('JOGO DOS ESTADOS'))   
print('-='*30)

acertos = erros = porcentagem = rodadas = 0
sair = False
while True:
    if sair == True:
        break
    for estado, capital in brasil.items():
        rodadas += 1
        resposta = str(input(f"\n-> Qual a capital do Estado '{estado}' ou digite <sair>? => ")).strip().lower()
        if resposta == 'sair':
            sair = True
            break
        if resposta == capital.lower():
            acertos += 1
            print("Resposta Correta!")
        else:
            erros += 1
            print(f"Resposta Errada! O correto seria {capital}.")

porcentagem = f"{acertos/rodadas *100:.2f}%"
print(f'\nAcertos: {acertos} | Errados: {erros} | Efetividade: {porcentagem}\n')



