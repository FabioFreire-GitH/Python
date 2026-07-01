from rich.panel import Panel
from rich import print

class ControleRemoto:
    """
    Classe que representa um controle remoto e suas funcionalidades
    """
    def __init__(self):
        """
        Atributos:
        :ligado: define se a TV está ligada ou desligada
        :canal: define qual canal a TV está
        :volume: define qual volume a TV está
        :controle: recebe o valor de entrada do uasuário
        """
        self.ligado = False
        self.canal = 0
        self.volume = 0
        self.controle = ""

    def selecionar_canal(self):
        """
        Seleciona qual canal está
        :return: string com o canal selecionado marcado
        """
        match self.canal:
            case 0:
                return f" [white on yellow] 1 [/]  2  3  4  5   "
            case 1:
                return f"  1  [white on yellow] 2 [/] 3  4  5   "
            case 2:
                return f"  1   2 [white on yellow] 3 [/] 4  5   "
            case 3:
                return f"  1   2  3 [white on yellow] 4 [/] 5   "
            case 4:
                return f"  1   2  3  4 [white on yellow] 5 [/]  "
            case _:
                return f" [bold red]Operação inválida[/]"

    def selecionar_volume(self):
        """
        Seleciona qual volume está
        :return: string com a barra e volume atual
        """
        match self.volume:
            case 0:
                return f"[cyan on cyan] [/][white on white]    [/]"
            case 1:
                return f"[cyan on cyan]  [/][white on white]   [/]"
            case 2:
                return f"[cyan on cyan]   [/][white on white]  [/]"
            case 3:
                return f"[cyan on cyan]    [/][white on white] [/]"
            case 4:
                return f"[cyan on cyan]     [/][white on white][/]"
            case _:
                return f" [bold red]Operação inválida[/]"

    def tv_desligada(self):
        """
        Apresenta mensagem de TV desligada
        :return: string formatado como PANEL com conteúdo de TV desligada
        """
        print(f'\n'*20)
        tv_desligada = Panel(":no_entry_sign: [red]A TV está desligada[/]", title='[ TV ]', title_align="center", width=35)
        print(tv_desligada)

    def tv_ligada(self):
        """
        Apresenta mensagem de TV ligada ataulizada
        :return: string foratado como PANEL com conteúdo de TV ligada atualizada
        """
        texto_canal = self.selecionar_canal()
        texto_volume = self.selecionar_volume()
        print(f'\n' * 20)
        tv_ligada = Panel(f"CANAL ={texto_canal}\nVOLUME ={texto_volume}", title='[ TV ]', title_align="center", width=35)
        print(tv_ligada)

    def comando(self):
        """
        Lê a entrada do usuário e atualiza os atributos do objeto
        :return: quando a entrada for "0", retona "True" para encerrar o program
        """
        controle = str(input("< CH 1 >  - VOL2 + "))

        match controle:
            case ">":
                if self.canal < 4:
                    self.canal += 1
                else:
                    self.canal = 0

            case "<":
                if self.canal > 0:
                    self.canal -= 1
                else:
                    self.canal = 4

            case "+":
                if self.volume < 4:
                    self.volume += 1
            case "-":
                if self.volume > 0:
                    self.volume -= 1
            case "@":
                self.ligado = not self.ligado

            case "0":
                return True

    def usar_tv(self):
        """
        Realiza loop do uso da televisão, sendo encerrado quando a variávl encerrar for True
        :return: void
        """
        encerrar = False
        while not encerrar:
            if self.ligado == False:
                self.tv_desligada()
            else:
                self.tv_ligada()
            encerrar = self.comando()

tv1 = ControleRemoto()
tv1.usar_tv()