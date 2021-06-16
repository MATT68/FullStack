#
#                      H E R E N C I A  
#
#    
#  Con esta característica, una clase puede heredar todos los atributos
#  y métodos de otra clase.
#  En Python esto se consigue al definir la clase, basta con añadir entre
#  paréntesis el nombre de la clase de la que queremos heredar.
#
#
#  Ejemplo :

class Telefono:
    def __init__ (self):
        self.__Numero    = 0        
        self.__Marca     = ' '        
        self.__Conectado = False
              
    def Conectar(self):
        self.__Conectado = True
        
    def Desconectar(self):
        self.__Conectado = False

    def Conectado(self):
        return self.__Conectado 

    def SetNumero(self,numero):
        self.__Numero  = numero

    def GetNumero(self):
        return self.__Numero  

    def SetMarca(self,marca):
        self.__Marca  = marca
        
    def GetMarca(self):
        return self.__Marca  

class Smartphone(Telefono):
    def __init__ (self):
        self.__HorasAutonomia = 0        
        self.__Pantalla       = 0

    def SetHorasAutonomia(self,horasautonomia):
        self.__HorasAutonomia  = horasautonomia
  
    def SetPantalla(self,pantalla):
        self.__Pantalla  = pantalla

    def MostrarSmartphone(self):
        print('>>>>>>>>>>>>>>>' )
        print(' Smartphone : ' )
        print(' Marca      : ',self.GetMarca() )
        print(' Número     : ',self.GetNumero() )
        print("\tHoras de Autonomia : ", self.__HorasAutonomia  )
        print("\tTamaño de pantalla : ", self.__Pantalla )
        if  self.Conectado() :
            print("\t Está conectado ! ")
        else:
            print("\t Está apagado ! ")
        
class Fijo(Telefono):
    def __init__ (self):
        self.__Direccion = ' ' 
        self.__CodPostal = 0
        
    def SetDireccion(self,direccion):
        self.__Direccion  = direccion
  
    def SetCodPostal(self,codpostal):
        self.__CodPostal  = codpostal

    def MostrarFijo(self):
        print('>>>>>>>>>>>>>>>' )
        print(' Teléfono Fijo : ' )
        print(' Marca      : ',self.GetMarca()    )
        print(' Número     : ',self.GetNumero()   )
        print("\tDirección  : ", self.__Direccion )
        print("\tCód.Postal : ", self.__CodPostal )
        if  self.Conectado() :
            print("\t Está conectado ! ")
        else:
            print("\t Está apagado ! ")
        
    
movil = Smartphone()                
movil.SetNumero(666888999)
movil.SetMarca('LG')                                  
movil.Conectar()
movil.SetHorasAutonomia(72)
movil.SetPantalla(5.4)
movil.MostrarSmartphone()
                  
fijo = Fijo()                
fijo.SetNumero(912223344)
fijo.SetMarca('Siemens')                                  
fijo.Conectar()
fijo.SetDireccion('Calle Castellana, 135')
fijo.SetCodPostal('00029')
fijo.MostrarFijo()

    
    
