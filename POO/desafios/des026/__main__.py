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

from funcionarios import *

def main():
    f1 = Horista("João", 12.00, 200)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista("Pedro", 9500)
    f2.calc_sal()
    f2.analisar_sal()



if __name__ == "__main__":
    main()

