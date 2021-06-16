#
#  Clase Punto, muestra la información
#       de las coordenadas de un punto
#
class Punto:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
        
    def MostrarPunto(self):
        print("El punto es (",self.X,",",self.Y,")")

p1 = Punto(4,6)
p1.MostrarPunto()
print('=========================>\n')

class Triangulo:
    def __init__ (self,v1,v2,v3):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3

    def MostrarVertices(self):
##        self.V1.MostrarPunto()
##        self.V2.MostrarPunto()
##        self.V3.MostrarPunto()
        v1.MostrarPunto()
        v2.MostrarPunto()
        v3.MostrarPunto()

print('=========================>\n')

v1 = Punto(0,0)
v2 = Punto(4,0)
v3 = Punto(2,2)
triangulo = Triangulo(v1,v2,v3)
triangulo.MostrarVertices()

