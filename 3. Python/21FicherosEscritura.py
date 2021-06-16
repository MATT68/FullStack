##############################################################
#
#        Escritura  de   F I C H E R O S    
#
##############################################################
#
#  - Después de hacer el open() ya podemos escritir.
#
#  Los modos de apertura son los siguientes :
#   “r”: abre el fichero para lectura.
#     ( Es el modo de apertura por defecto )
#   “w”: abre el fichero para escritura truncándolo.
#   “x”: crea un fichero para escribir (no debe existir).
#   “a”: append - situa el cursor de escritura al final.
#   “b”: abre en modo binario.(fotos, exe, etc.
#   “t”: abre en modo fichero de texto (es el defecto).
#   “+”: abre el fichero para lectura y escritura.
#
#   Vamos a comprobar los diferentes efectos de los modos
#   de apertura.
#
#   ESCRITURA DE FICHEROS EN MODO APPEND ("a")
#
print(">>>>  Fichero ejemplo.txt A N T E S      de escribir :   <<<<")
fichero1 = open("ejemplo.txt","r")
texto = fichero1.read()
print(texto)
fichero1.close()
#
ficherow = open("ejemplo.txt","a")
ficherow .write("Linea escrita desde el programa.\n")
ficherow.close()
print(">>>>  Fichero ejemplo.txt D E S P U E S   de escribir :   <<<<")
fichero1 = open("ejemplo.txt","r")
texto = fichero1.read()
print(texto)
fichero1.close()
#
#   ESCRITURA DE FICHEROS EN MODO TRUNCADO ("w")
#
print(">>>>  Fichero ejemplo.txt A N T E S      de escribir :   <<<<")
fichero1 = open("ejemplo.txt","r")
texto = fichero1.read()
print(texto)
fichero1.close()
#
ficherow = open("ejemplo.txt","w")
ficherow .write("Linea escrita desde el programa.\n")
ficherow.close()
print(">>>> Fichero ejemplo.txt D E S P U E S   de escribir :   <<<<")
fichero1 = open("ejemplo.txt","r")
texto = fichero1.read()
print(texto)
fichero1.close()
#
#   ESCRITURA DE FICHEROS EN MODO NOT EXISTS ("x")
#
ficherow = open("ejemplo3.txt","x")
ficherow .write("1 Linea escrita desde el programa.\n")
ficherow .write("2 Linea escrita desde el programa.\n")
ficherow .write("3 Linea escrita desde el programa.\n")
ficherow .write("4 Linea escrita desde el programa.\n")
ficherow.close()
print(">>>> Fichero ejemplo3.txt D E S P U E S   de escribir :   <<<<")
fichero1 = open("ejemplo3.txt","r")
texto = fichero1.read()
print(texto)
fichero1.close()
#
#  AL ESCRIBIR, PRESTAR ATENCION AL CARACTER DE FIN DE LINEA 
#
ficherow = open("ejemplo3.txt","a")
ficherow .write("1 Linea escrita desde el programa.")
ficherow .write("2 Linea escrita desde el programa.\t")
ficherow .write("3 Linea escrita desde el programa.")
ficherow .write("4 Linea escrita desde el programa.\t")
ficherow.close()
print(">>>> Fichero ejemplo3.txt D E S P U E S   de escribir :   <<<<")
fichero1 = open("ejemplo3.txt","r")
texto = fichero1.read()
print(texto)
fichero1.close()
