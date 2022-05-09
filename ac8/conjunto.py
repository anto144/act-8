class Conjunto:
    __lista = []

    def __init__(self):
        self.__lista = []

    def cargar(self):
        self.__lista = []
        print("INGRESE LOS ELEMENTOS DEL CONJUNTO, PARA FINALIZAR INGRESE: 0")
        while True:
            elem = int(input("ELEMENTO: "))
            if(elem == "0"):
                break
            self.__lista.append(elem)
            self.__lista.sort()
        print("CONJUNTO CARGADO CON EXITO")


    def mostrarConj(self):
        print("CONJUNTO: ")
        print(self.__lista)
    
    def __add__(self, other):
        conjunto = Conjunto()
        for elem in self.__lista:
            conjunto.__lista.append(elem)
        for elem in other.__lista:
            if(elem not in conjunto.__lista):
                conjunto.__lista.append(elem)
        return conjunto
    
    def __sub__(self, other):
        conjunto = Conjunto()
        for elem in self.__lista:
            if(elem not in other.__lista):
                conjunto.__lista.append(elem)
        return conjunto
    
    def __eq__(self, other):
        for elem in self.__lista:
            if(elem not in other.__lista):
                return False
        return True