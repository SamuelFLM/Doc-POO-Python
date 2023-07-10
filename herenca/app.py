class Funcionario:
    def __init__(self, nome, cpf, salario) -> None:
        self._nome = nome
        self._cpf = cpf
        self._salario = salario


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_subordinados) -> None:
        Funcionario.__init__(self, nome, cpf, salario)
        self._senha = senha
        self._qtd_subordinados = qtd_subordinados

    def validacao(self, senha):
        if self._senha == senha:
            print("Acesso permitido.")
            return True
        else:
            print("Acesso negado.")
            return False


class Secretaria(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerentes):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerentes = qtd_gerentes

s1 = Secretaria("Julia", 1000, 5000, 12345, 5)

print(s1._nome)