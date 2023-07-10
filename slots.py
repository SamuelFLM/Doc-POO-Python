class Pessoa():
    
    _num_pessoas = 0
    
    __slots__ = ["__idade"] #Aqui informo as variaveis fixa da class construtora, nao permitindo a atribuicao de novas
    
    def __init__(self, idade:int) -> None:
        self.__idade = idade
        Pessoa._num_pessoas += 1
        
    @classmethod
    def get_num_pessoas(cls):
        return cls._num_pessoas


if __name__ == "__main__":
    p1 = Pessoa(20)
    
    print(dir(p1))