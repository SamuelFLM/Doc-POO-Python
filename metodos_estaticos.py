

class Pessoa():
    
    _num_pessoas = 0
    
    def __init__(self, idade:int) -> None:
        self.__idade = idade
        Pessoa._num_pessoas += 1
        
    @staticmethod
    def get_num_pessoas():
        return Pessoa._num_pessoas


if __name__ == "__main__":
    p1 = Pessoa(20)
    p1 = Pessoa(20)
    p1 = Pessoa(20)
    
    print(Pessoa.get_num_pessoas())
    
    print(p1.get_num_pessoas())