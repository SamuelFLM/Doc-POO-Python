class Televisao:
    # Atributos privados

    def __init__(self, cor: str, resolucao: int, tamanho: str) -> None:
        self.__cor = cor
        self.__resolucao = resolucao
        self.__tamanho = tamanho

    """_summary_
    
    O property get faz o metodo se torna uma propriedade(Atributo)..
    Nao precisando colocar o () de metodo
    Returns:
        _type_: _description_
    """

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor: str):
        self.__cor = cor

    # Metodos para manipular os atributos

    def getCor(self):
        return self.__cor

    def setCor(self, cor: str):
        self.__cor = cor.title()

    ## outra maneira

    def getResolucao(self):
        return self.__resolucao

    def setResolucao(self, nova_resolucao: str):
        self.__resolucao = nova_resolucao

    resolucao = property(fget=getResolucao, fset=setResolucao)


if __name__ == "__main__":
    televisao = Televisao("Branco", 20, "200px")
    print(televisao.cor)
    televisao.cor = "Azul"
    print(televisao.cor)
     
    print(televisao.resolucao )
    televisao.resolucao = 50
    print(televisao.resolucao )
