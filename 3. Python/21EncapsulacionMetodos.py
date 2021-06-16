#
#   E N C A P S U L A C I O N 
#
#    
#  Métodos:
#  También se encapsulan métodos. Los métodos privados sólo pueden accederse
#  desde el propio objeto. 
#
#  Sintaxis: para definir un método como privado debemos poner
#  __  delante del nombre
#
#  Ejemplo :

class Tertuliano:
    def __init__ (self,nombre,apellidos,telefono):
        self.__Nombre    = nombre
        self.__Apellidos = apellidos        
        self.__Telefono  = telefono
        
    def __MostrarNombre(self):
        print(" Nombre : ",self.__Nombre)
    def __MostrarApellidos(self):
        print(" Apellidos : ",self.__Apellidos)
    def __MostrarTlf(self):
        print(" Tlf : ",self.__Telefono)

    def MostrarTertualiano(self):
        self.__MostrarNombre()
        self.__MostrarApellidos()
        self.__MostrarTlf()

tertuliano = Tertuliano('Pipi','Estrada Nosenfada','669899777')
tertuliano.MostrarTertualiano()
# Si intentamos acceder al método privado __MostrarNombre() sucede que :
tertuliano.__MostrarNombre()
tertuliano.MostrarTertualiano()
