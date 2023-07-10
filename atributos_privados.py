
class Payments():
    
    def __init__(self) -> None:
        self.__privado = "Samuel" #Torna privado
        self.publico = "Publico"

    def pagar_client(self):
        self.__privado = "Pagando"
        print(self.__privado)
        self.__metodo_privado()
        
    def __metodo_privado(self):
        print("Meu metodo privado")

if __name__ == "__main__":
    payments = Payments()
    print(payments.publico)
    print(payments._Payments__privado) # Acessando variaveis privadas
    payments.pagar_client()
    
    #Metodo privado
    # payments._Payments__metodo_privado()
    