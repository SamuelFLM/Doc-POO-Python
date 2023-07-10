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

if __name__ == "__main__":
    
    g1 = Gerente("Lucas", 987, 5600, 1234, 10)
    
    s1 = Secretaria("Renata", 345, 4000, 789, 5)
    
    bonus = g1.mostrar_bonus()
    print("Bonus gerente: " + str(bonus))
    bonus = s1.mostrar_bonus()
    print("Bonus secretaria: " + str(bonus))
    