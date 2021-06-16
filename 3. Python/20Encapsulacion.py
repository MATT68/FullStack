#
#   E N C A P S U L A C I O N 
#
#  Podemos definir los datos (atributos) que forman una clase como :
#  
#       Públicos : se pueden acceder directamente desde fuera de la clase
#       Privados : se pueden acceder desde fuera pero de forma controlada
# 
#  Atributos:
#  Para encapsular datos los definimos como privados y definimos un método
#  para acceder a ellos.
#    
#  Métodos:
#  También se encapsulan métodos. Los métodos privados sólo pueden accederse
#  desde el propio objeto. 
#
#  Sintaxis: para definir un atributo como privado debemos poner
#  __ después de self y delante del nombre
#
#  Ejemplo :
#
#  Cómo poder ver los valores privados ? 
#  Para la clase que tiene los atributos como privados es necesario que
#  incluyas los métodos para leer (normalmente se usa como nombre del método
#  Get unido al nombre del atributo) y para escribir (normalmente se usa
#  como nombre del método Set unido al nombre del atributo).
#  
#  La clase Tertuliano quedaría así:
print(" ============ p r i v a d o ============== > ")

class Tertuliano:
    def __init__ (self,nombre,apellidos,telefono):
        self.__Nombre    = nombre
        self.__Apellidos = apellidos        
        self.__Telefono  = telefono
        
    def GetNombre(self):
        return self.__Nombre
    def GetApellidos(self):
        return self.__Apellidos
    def GetTelefono(self):
        return self.__Telefono
    def SetNombre(self,nombre):
        self.__Nombre    = nombre
    def SetApellidos(self,apellidos):
        self.__Apellidos = apellidos        
    def SetTelefono(self,telefono):
        self.__Telefono  = telefono
    
    def MostrarTertuliano(self):
        print(" Tertuliano : ",self.__Nombre,self.__Apellidos,":",self.__Telefono)

tertuliano = Tertuliano('Coto','Matamoros Todolosabe','666999777')
tertuliano.MostrarTertuliano()
# Ahorna no podremos ver Nombre y Telefono si no es llamando al método anterior
print(" Nombre Tertuliano : ",tertuliano.GetNombre(),'-',tertuliano.GetTelefono())

