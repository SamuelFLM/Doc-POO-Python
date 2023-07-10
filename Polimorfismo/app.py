class Funcionario:
    def __init__(self, nome, cpf, salario) -> None:
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def mostrar_bonus(self):
        return self._salario * 0.10

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_subordinados) -> None:
        Funcionario.__init__(self, nome, cpf, salario)
        self._senha = senha
        self._qtd_subordinados = qtd_subordinados

    def mostrar_bonus(self):
        return self._salario * 0.10 + self._qtd_subordinados * 0.10
    
class Secretaria(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerentes):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerentes = qtd_gerentes
        
    def mostrar_bonus(self):
        return self._salario * 0.10 + self._qtd_gerentes * 0.10


class Engenheiro():
    
    def __init__(self, nome) -> None:
        self._nome = nome

class GestaoDeBonus():
    
    def __init__(self, total_bonificacoes = 0) -> None:
        self._total_bonificacoes = total_bonificacoes
        
    def registrar(self, funcionario):
        # Realiza um tratamento para verificar se o Objeto adicionado tem o metodo mostrar_bonus
        if(hasattr(funcionario, 'mostrar_bonus')):
            self._total_bonificacoes += funcionario.mostrar_bonus()
        else:
            print("Objeto adicionado {} nao tem implementado o método mostrar_bonus".format(self.__class__.__name__))
            
    def registrar_isistance(self, funcionario1):
        # Realiza um tratamento para verificar se o Objeto adicionado tem o metodo mostrar_bonus
        if(isinstance(funcionario1, Funcionario)):
            self._total_bonificacoes += funcionario1.mostrar_bonus()
        else:
            print("Objeto adicionado {} nao tem implementado o método mostrar_bonus".format(self.__class__.__name__))
        
    @property
    def total_bonificacoes(self):
        return f'{self._total_bonificacoes}'
        
        

if __name__ == "__main__":
    
    g1 = Gerente("Lucas", 987, 5600, 1234, 10)
    
    s1 = Secretaria("Renata", 345, 4000, 789, 5)
    
    e1 = Engenheiro("Samuel")
    #s2 = Secretaria("Julia", 345, 4000, 789, 5)
    
    gestao =  GestaoDeBonus()
    
    #gestao.registrar(e1)
    gestao.registrar_isistance(g1)
    
    gestao.registrar(g1)
    gestao.registrar(s1)
    
    print(gestao.total_bonificacoes)
    
    # bonus = g1.mostrar_bonus()
    # print("Bonus gerente: " + str(bonus))
    # bonus = s1.mostrar_bonus()
    # print("Bonus secretaria: " + str(bonus))
    