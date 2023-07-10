"""_summary_

    @classmethod (Entra na herenca)
    @staticmethod (Nao entra na herenca)

"""



class Pessoa():
    
    _num_pessoas = 0
    
    def __init__(self, idade:int) -> None:
        self.__idade = idade
        Pessoa._num_pessoas += 1
    
    @classmethod
    def get_num_pessoas(cls):
        return cls._num_pessoas


if __name__ == "__main__": 
    p1 = Pessoa(20)
    p1 = Pessoa(20)
    p1 = Pessoa(20)
    
    print(Pessoa.get_num_pessoas())
    
    print(p1.get_num_pessoas())