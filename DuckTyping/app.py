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

class ClubeGerente():
    def __init__(self, nome, funcionarios) -> None:
        self.nome = nome
        self._funcionarios = funcionarios
    
    # Faz a class se comportar como uma lista
    def __getitem__(self, item):
        return self._funcionarios[item]

    def __len__(self):
        return len(self._funcionarios)
    
    def add_item(self, item):
        self._funcionarios.append(item)
    
g1 = Gerente("Lucas", 876, 1200, 143, 10)
g2 = Gerente("Pedro", 246, 5200, 163, 20)
g3 = Gerente("Ricardo", 866, 2200, 423, 15)


lista_gerentes = [g1, g2, g3]

clube = ClubeGerente('ClubeTop', lista_gerentes)

print(len(clube))
print(clube[0]._nome)

for g in clube:
    print(g._nome)
    
clube.add_item(Gerente("Rafael", 866, 2200, 423, 15))

print(clube[3]._nome)