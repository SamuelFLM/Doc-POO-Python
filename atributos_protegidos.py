class Televisao:
    # Atributos privados

    def __init__(self, cor: str, resolucao: int, tamanho: str) -> None:
        self._cor = cor #Atributo protegido
        self._resolucao = resolucao #Atributo protegido
        self.__tamanho = tamanho #Atributo privado

    # Metodos para manipular os atributos

    #Metodo protegido
    def _tamanho_resolucao(self):
        pass
    #Metodo privado
    def __tamanho_resolucao_privado(self):
        pass

    def getCor(self):
        return self.__cor

    def setCor(self, cor: str):
        self.__cor = cor.title()
