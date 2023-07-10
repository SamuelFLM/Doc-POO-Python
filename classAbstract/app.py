import abc
from collections.abc import MutableSequence

# herença de uma class abstrata
class ClubeSecretarias(MutableSequence):
    pass

# Criando uma class abstrata
class Funcionario(abc.ABC):

    @abc.abstractmethod
    def nome(self):
       print('nome')
       
    @abc.abstractmethod
    def senha(self):
       print('senha')


# O que e uma interface?

class Atendente(Funcionario):
    
    def nome(self):
       print('nome')
       
    def senha(self):
       print('senha')

f = Atendente()