#
#  Clase Punto, muestra la información
#       de las coordenadas de un punto
#
print('=========== 1 ============>\n')
class Punto:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
        
    def MostrarPunto(self):
        print("El punto es (",self.X,",",self.Y,")")

p1 = Punto(4,6)
p1.MostrarPunto()
print('=========== 2 ============>\n')
#
#   Creamos cuatro objetos de la clase Punto.
#
p1 = Punto(4,6)
p2 = Punto(-5,9)
p3 = Punto(3,-7)
p4 = Punto(0,4)
p1.MostrarPunto()
p2.MostrarPunto()
p3.MostrarPunto()
p4.MostrarPunto()
print('=========== 3 ============>\n')
#
#   Reasignamos un valor del objeto
#
class Punto:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y

    def MostrarPunto(self):
        print("El punto es (",self.X,",",self.Y,")")

p1 = Punto(4,6)
p1.MostrarPunto()
print('Las coordenadas son :', p1.X,p1.Y)
p1.X = 7
p1.MostrarPunto()
print('=========== 4 ============>\n')
#
#   Reasignando objetos se reasignan sus valores.
#
class Punto:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y

    def MostrarPunto(self):
        print("El punto es (",self.X,",",self.Y,")")

p1 = Punto(4,6)
p1.MostrarPunto()
p2 = Punto(3,8)
p2.MostrarPunto()
p1 = p2
p1.MostrarPunto()
print('==========================>\n')

