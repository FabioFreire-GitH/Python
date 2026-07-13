
class Tabuleiro:
    def __init__(self):
        self._grade = [['','',''],['','',''],['','','']]

    def marcar_jogada(self, linha, coluna, simbolo):
        if 0 <= linha < 3 and 0 <= coluna < 3:
            if self.verificar_vazio(linha, coluna):
                self._grade[linha][coluna] = simbolo
                return True
            else:
                print("ERRO: Posição já ocupada. Tente novamente.")
                return False
        else:
            print("ERRO: Linha ou coluna fora dos limites (0, 1 ou 2). Tente novamente.")
            return False
        
    
    def verificar_vazio(self, linha, coluna):
        if 0 <= linha < 3 and 0 <= coluna < 3:
            return self._grade[linha][coluna] == ''     
        else:
            return False
                

    def verificar_vitoria(self, simbolo):
        # - Verifica Linhas
        for linha in self._grade:
            if all(celula == simbolo for celula in linha):
                return True
        # - Verifica Colunas
        for j in range(3):
            if all(self._grade[i][j] == simbolo for i in range(3)):
                return True
        # - Verifica Diagonais
        # -- Diagonal Principal
        if self._grade[0][0] == simbolo and self._grade[1][1] == simbolo and self._grade[2][2] == simbolo:
            return True
        # -- Diagonal Secundária
        if self._grade[0][2] == simbolo and self._grade[1][1] == simbolo and self._grade[2][0] == simbolo:
            return True
        
        return False

    def verificar_empate(self):
        for linha in self._grade:
            if any(celula == '' for celula in linha):
                return False
        return True


    def __str__(self):
        conteudo = f'   {'0':^3}  {'1':^6} {'2':^6}\n'
        conteudo += "-"*22 + "\n"
        for i, linha in enumerate(self._grade):
            conteudo += f"{i} - {linha[0] if linha[0] else ' ':^3} | {linha[1] if linha[1] else ' ':^3} | {linha[2] if linha[2] else ' ':^3}\n"
            if i < 2:
                conteudo += '-'*22 + "\n"
        return conteudo
         

class Jogador:
    def __init__(self, nome, simbolo):
        self._nome = nome
        self._simbolo = simbolo

    def get_nome(self):
        return self._nome

    def get_simbolo(self):
        return self._simbolo


class JogoDaVelha:
    def __init__(self, nome_jogador1, nome_jogador2, simbolo_jogador1 = 'X', simbolo_jogador2 = 'O'):
        self._tabuleiro = Tabuleiro() # Cria uma instância do tabuleiro
        self._jogador1 = Jogador(nome_jogador1, simbolo_jogador1)
        self._jogador2 = Jogador(nome_jogador2, simbolo_jogador2)
        self._jogador_atual = self._jogador1 # Começa com o jogador 1
            
    def iniciar_jogo(self):
        while True:
            print(self._tabuleiro)
            print(f"Vez de {self._jogador_atual.get_nome()} ({self._jogador_atual.get_simbolo()}).")
            
            jogada_valida = False
            while not jogada_valida:
                try:
                    # entrada dos dados
                    l_str = input('Escolha linha (0 a 2): ')
                    c_str = input('Escolha coluna (0 a 2): ')

                    # conversão dos dados - se falhar, em ValueError acontece aqui
                    l = int(l_str)
                    c = int(c_str)

                    # tenta marcar a jogada. Retorna True se a jogada for bem sucedida
                    if self._tabuleiro.marcar_jogada(l, c, self._jogador_atual.get_simbolo()):
                        jogada_valida = True
                except ValueError:
                    print("Entrada inválida. Por favor, digite números para linha e coluna.")
            
            if self._tabuleiro.verificar_vitoria(self._jogador_atual.get_simbolo()):
                print(self._tabuleiro)
                print(f"{self._jogador_atual.get_nome()} venceu!")
                break
            elif self._tabuleiro.verificar_empate():
                print(self._tabuleiro)
                print("O jogo terminou em empate!")
                break
            self._alternar_jogadores()
           
  
    def _alternar_jogadores(self):
        if self._jogador_atual == self._jogador1:
            self._jogador_atual = self._jogador2
        else:
            self._jogador_atual = self._jogador1


if __name__ == '__main__':
    jogo = JogoDaVelha('Jogador1', 'Jogador2')
    jogo.iniciar_jogo()



