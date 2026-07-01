import time
import sys

def pergaminho_com_borda(texto, atraso=0.03):
    linhas = texto.split('\n')
    # Descobre o comprimento da linha mais longa para ajustar a largura do pergaminho
    largura = max(len(linha) for linha in linhas) + 4

    # Topo do pergaminho
    topo = f" 📜  {'_' * largura} \n    (  {'_' * (largura-2)}  )\n     ) { ' ' * (largura-2) } ("
    print(topo)

    # Conteúdo com as bordas laterais e o efeito de digitação
    for linha in linhas:
        # Preenche com espaços vazios para alinhar a borda direita perfeitamente
        linha_formatada = f"     |  {linha.ljust(largura-4)}  |"
        
        # Aplica o efeito letra por letra apenas no texto interno
        for letra in linha_formatada:
            sys.stdout.write(letra)
            sys.stdout.flush()
            time.sleep(atraso)
        print()

    # Fundo do pergaminho
    fundo = f"    (_{'_' * (largura-2)}_) \n  📜   {')' + '_' * (largura-3) + ')'}"
    print(fundo)
    time.sleep(0.5)

# --- EXEMPLO DE USO NO SEU DUELO ---

mensagem_duelo = (
    "⚔️  O DUELO COMEÇOU!  ⚔️\n"
    "Você puxa sua lâmina reluzente.\n"
    "O Cavaleiro Negro avança com fúria!"
)

pergaminho_com_borda(mensagem_duelo)
