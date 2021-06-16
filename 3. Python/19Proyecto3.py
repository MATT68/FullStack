##############################################################
#
#   Proyecto Biblioteca
#
##############################################################
#
#  Definimos tres clases: Autor, Libro y Biblioteca.
#
#  La clase Autor contiene los siguientes:
#  Atributos:
#       Nombre    : nombre   del escritor
#       Apellido1 : apellido1 del escritor
#       Apellido2 : apellido2 del escritor
#
#  Métodos:
#  MostrarAutor : mostrará los atributos Nombre y Apellidos
#
class Autor:
    def __init__ (self,nombre,apellidos):
        self.Nombre    = nombre
        self.Apellidos = apellidos
        
    def MostrarAutor(self):
        print("Autor :",self.Apellidos,",",self.Nombre)

# $$$$$$$$$$$$$$$$$
# $p1 = Autor("Arturo","Perez Reverte")
# $p1.MostrarAutor()
# $print('=========================>\n')
# $$$$$$$$$$$$$$$$$

#
#  La clase Libro contiene los siguientes:
#  Atributos:
#       Titulo   : nombre del libro
#       ISBN     : identificador del libro
#       Autor    : atributo del tipo Autor
#
#  Métodos:
#       AgregarAutor   : guardará la información del autor en el atributo Autor
#       MostrarLibro   : mostrará por pantalla la información del Libro
#       ObtenerTitulo  : devolverá el título del libro
#
class Libro:
    def __init__ (self,titulo,isbn):
        self.Titulo = titulo
        self.ISBN   = isbn

    def AgregarAutor(self,autor):
        self.Autor = autor
        
    def MostrarLibro(self):
        print("------ Libro ------")
        print("Titulo: ",self.Titulo)
        print("ISBN: ", self.ISBN)
        self.Autor.MostrarAutor()
        print("-------------------")
        
    def ObtenerTitulo(self):
        return self.Titulo;

#
#  La clase Biblioteca:
#  Atributos:
#       ListaLibros : atributo de tipo lista que contiene todos los
#                     libros que componen la biblioteca
#  Métodos:  
#       NumeroLibros: devuelve el número de libros que hay en la biblioteca
#       AgregarLibro: almacena el libro pasado por parámetro en la lista 
#       BorrarLibro : borra un libro de la biblioteca a partir del título
#       MostrarBiblioteca : mostrará por pantalla todos los libros que
#                     componen la biblioteca
#

class Biblioteca:
    def __init__ (self):
        self.ListaLibros = []
        
    def NumeroLibros(self):
        return len(self.ListaLibros)
    
    def AgregarLibro(self,libro):
        self.ListaLibros = self.ListaLibros + [libro]       

    def MostrarBiblioteca(self):
        print('=========================>\n')
        for i in self.ListaLibros:
            i.MostrarLibro()
        print('=========================>\n')
        
    def BorrarLibro(self,titulo):
        encontrado = False
        posicionaborrar = -1
        for item in self.ListaLibros:
            posicionaborrar += 1
            if  item.ObtenerTitulo() == titulo:
                encontrado = True
                break
            
        if  encontrado:
            del self.ListaLibros[posicionaborrar]
            print(' Libro borrado correctamente ! ')
        else:
            print(' Libro no encontrado ! ')

#
#  El proyecto tendrá las siguientes funciones:
#
#      MostrarMenu: mostrará el menú de opciones al usuario para
#           que elija lo que quiere hacer.
#      AgregarLibroABiblioteca: función que realizará el flujo de dar
#           de alta un nuevo libro en la biblioteca,
#           pidiendo toda la información necesaria para un libro.
#      MostrarBiblioteca: función que utilizando el método MostrarBiblioteca
#           de la clase Biblioteca mostrará la información de todos los
#           libros que componen la biblioteca.
#      BorrarLibro: función que realizará el flujo de dar de baja (borrar)
#           un libro de la biblioteca.
#      NumeroLibros: función que mostrará el número de libros que componen
#           la biblioteca.
#
#      
def MostrarMenu():
    print ("""
    =======      Menu   ============
    1) Añadir libro a la biblioteca
    2) Mostrar biblioteca
    3) Borrar libro
    4) Quieres saber el numero de libros?
    5) Salir
    =======             ============
    """)

def AgregarLibroABiblioteca(biblioteca):
    titulo      = input( "Introduce el título del libro: ")
    isbn        = input( "Introduce el ISBN  del libro: ")
    autornombre = input( "Introduce el nombre del autor: ")
    autorapellido  = input( "Introduce el apellido(s) del autor: ")
    libro1 = Libro(titulo,isbn)
    autor1 = Autor(autornombre,autorapellido)
    libro1.AgregarAutor(autor1)
    biblioteca.AgregarLibro(libro1)
    return biblioteca

def MostrarBiblioteca(biblioteca):
    biblioteca.MostrarBiblioteca()

def BorrarLibro(biblioteca):
    titulo = input("Dime el título del libro a borrar: ")
    biblioteca.BorrarLibro(titulo)

def NumeroLibros(biblioteca):
    print(" El número de libros en la biblioteca es : ",
          biblioteca.NumeroLibros() ) 
                   
fin = False    

biblioteca = Biblioteca()

while not fin:
    MostrarMenu()
    opcion = int(input("Seleccione opción : "))
    if  opcion == 1:
        AgregarLibroABiblioteca(biblioteca)
    elif  opcion == 2:
          MostrarBiblioteca(biblioteca)
    elif  opcion == 3:
          BorrarLibro(biblioteca)
    elif  opcion == 4:
          NumeroLibros(biblioteca)
    elif  opcion == 5:
          fin = True        
    else: 
          print ("Opción no válida ... ")

print(" Gracias por jugar ! ")
        





