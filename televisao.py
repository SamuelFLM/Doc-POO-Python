
#Forma correta

class Televisao():
    
    
    #Atributos privados
    
    def __init__(self, cor:str , resolucao:int, tamanho:str) -> None:
        self.__cor = cor
        self.__resolucao = resolucao
        self.__tamanho = tamanho
    
    #Metodos para manipular os atributos
        
    def getCor(self):
        return self.__cor
    
    def setCor(self, cor: str):
        self.__cor = cor.title()
    