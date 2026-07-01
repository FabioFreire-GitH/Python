# DESAFIO 026: Crie a estrutura capaz de calcular salários de funcionarios diferentes
'''
-------------------------------------------------
            Funcionario{abstract}
-------------------------------------------------
            + nome
            + sal_bruto
            + salario
            + sal_min = 1612
            + inss = 7.5
-------------------------------------------------
            + calc_sal(){abstract}
            + analisar_sal()
-------------------------------------------------

        ^                  ^       
        |                  |       
--------------     ------------------ 
    Horista             Mensalista
--------------     ===================
+ valor_hora        + + calc_sal()
+ horas_trab       -------------------
--------------     
+ calc_sal()      

'''
from abc import ABC, abstractmethod
from rich import print, inspect
from rich.panel import Panel

class Funcionario(ABC):

    sal_min:float = 1612.00
    inss:float = 7.5/100

    def __init__(self, nome = None, salario_bruto=0):
        self.nome:str = nome
        self.sal_bruto:float = salario_bruto
        self.salario:float = 0
        

    def analisar_sal(self):
        conteudo = f"O salário de [blue]{self.nome}[/] ([cyan]{self.__class__.__name__}[/]) é [green]R$ {self.salario:.2f}[/] líquido, "
        conteudo += f"e corresponde a [yellow]{(self.salario/Funcionario.sal_min):.1f} salários minimos[/]." 
        analise = Panel(conteudo, title= "Análise de Salário", width= 50)
        return print(analise)

    @abstractmethod
    def calc_sal(self):
        pass


class Horista(Funcionario):
    def __init__(self,nome ,valor_hora = 7.37, qtd_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = qtd_horas

    def calc_sal(self):
        self.salario = self.horas_trab * self.valor_hora
        self.salario -= self.salario * Funcionario.inss
            

class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome, salario_bruto)
        

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss)
            