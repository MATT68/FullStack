##############################################################
#
#      C O N T R O L      D E     E X C E P C I O N E S   
#
##############################################################
#
#  Cuando en un programa se produce un error (exception) es necesario
#  controlarlo para dar un mensaje aproximado de lo sucedido.
#  
#  En algunos casos podría continuar la ejecución del programa después
#  de controlar la excepción, pero en muchos se detendrá la ejecución.
#
#  Es necesario incluir el el código fuente de ejecución normal dentro 
#  de un bloque con la sentencia try, posteriormente, posteriormente, 
#  se crea un bloque de código dentro de una sentencia except que es 
#  la que se ejecutará en caso de error. 
#   El bloque except permite especificar el tipo de error que se controla 
#  con el bloque de código, es por ello por lo que puedes tener tantos 
#  bloques except como errores quieras controlar, aunque también es 
#  posible controlar un error genérico que incluya a todos los errores. 
#   En el control de excepciones existe la posibilidad de crear un bloque
#  de código que se ejecute siempre al final, independientemente de si 
#  ocurre error o no, dicho bloque de código se escribe como parte de la 
#  sentencia finally. 
#  El control de excepciones en Python tiene un aspecto así: 
#  
#  try: BloqueInstruccionesPrograma 
#  except TipoError1: BloqueInstruccionesError1 
#  except TipoError2: BloqueInstruccionesError2
#  except TipoErrorN: BloqueInstruccionesErrorN 
#  finally: ​BloqueCodigoFinally
#
#
#  Vemos un contro de errores sencillo : 
try:
    nombre_file = "FileNoExiste.txt"
    fichero1 = open(nombre_file,"r")
except:
    print("**   No existe el fichero  1 ** ")
#
#
#  Agregamos la sentencia finally para que siempre muestre el fin
#  del programa. 
#
try:
    nombre_file = "FileNoExiste.txt"
    fichero1 = open(nombre_file,"r")
except:
    print("**   No existe el fichero  2 ** ")

finally: 
    print(" F I N     D E     P R O G R A M A   ")
#
#   Podemos controlar las excepciones individualmente.
#   Este código falla porque no existe el fichero. 
#
#
try:
    nombre_file = "FileNoExiste.txt"
    fichero1 = open(nombre_file,"r")
except FileNotFoundError:
    print("******************************")
    print("**       E  R  R  O  R      **")
    print("**   No existe el fichero 3 ** ")
    print("******************************")
else:    
    texto = fichero1.read()
    print(texto)
    fichero1.close()
finally: 
    print(" F I N     D E     P R O G R A M A   ")
#
#
#   Y funciona cuando existe
#
#
try:
    nombre_file = "ejemplo.txt"
    fichero1 = open(nombre_file,"r")
except FileNotFoundError:
    print("******************************")
    print("**       E  R  R  O  R      **")
    print("**   No existe el fichero 4 ** ")
    print("******************************")
else:    
    texto = fichero1.read()
    print(texto)
    fichero1.close()
finally: 
    print(" F I N     D E     P R O G R A M A   ")
#
#
#   Pero deberíamos completarlo controlando cualquier error
#
#
try:
    nombre_file = "ejemplo.txt"
    fichero1 = open(nombre_file,"r")
except FileNotFoundError:
    print("******************************")
    print("**       E  R  R  O  R      **")
    print("**   No existe el fichero 5 ** ")
    print("******************************")
except:
    print("********************************")
    print("**         E  R  R  O  R      **")
    print("** Ahora no podemos atenderte ** ")
    print("********************************")    
else:    
    texto = fichero1.read()
    print(texto)
    fichero1.close()
finally: 
    print(" F I N     D E     P R O G R A M A   ")
#
