#DESAFIO 29: Simule um diario secreto orientado a objetos.
'''
----------------   
    Diario
----------------     
- __segredos[]
- __senha
----------------
+ escrever(msg)
+ ler (msg)
----------------    
'''
class Diario:
    def __init__(self, senha = "1234"):
        self.__segredos = []
        self.__senha = senha.strip()
        

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, senha = None):
        if senha is None or senha == "":
            raise TypeError("Senha não informada! Diario bloqueado!")
        if senha != self.__senha:
            raise ValueError("Senha incorreta! Diario bloqueado!")
        linhas = []
        linhas.append("--- Diario Liberado ---")
        for c, item in enumerate(self.__segredos):
            linhas.append(f"{c+1} - {item}")
        
        linhas.append("--- Fim de Diário ---")
        return "\n".join(linhas) # Junta todas as linhas com uma quebra de linha
    
    @property
    def senha(self):
        raise PermissionError("Sem permissão de ler a senha!")
    
    @senha.setter
    def senha(self, novasenha):
        pass
    
    

