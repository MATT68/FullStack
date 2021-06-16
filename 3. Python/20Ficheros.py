##############################################################
#
#    Tratamiento   de   F I C H E R O S    
#
##############################################################
#
#  En Python podemos usar ficheros para leer o 
#  almacenar información en el disco duro.
#  
#  Los pasos para leer un fichero son:
#    - Abrir  fichero (para poder leer)
#    - Leer   fichero (total o parcialmente)
#    - Cerrar fichero (al acabar la lectura)
#  Los pasos para escribir son los mismos, pero cambiando
#  la función de lectura por la de escritura.
#      
#
#  Así que con las funciones open, close, read y write 
#  podemos hacer todo el tratamiento de los ficheros.
#
#  La función open tiene dos parámetros de entrada:
#  - Ruta del fichero que se desea abrir.
#  - Modo de apertura del fichero.
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
#  Lectura de fichero completo
#
print(">>>>   1.- Lectura de fichero completo  <<<<")
fichero1 = open("ejemplo.txt","r")
texto = fichero1.read()
print(texto)
fichero1.close()
#
#   Lectura del fichero linea a linea con bucle for:
#
print(">>>>   2.- Lectura de fichero con bucle  <<<<")
for linea in open("ejemplo.txt","r"):
    print(linea)
#
#   Lectura con método readline().
# 
#   El comando readline lee una línea y deja el cursor
#   posicionado en la siguiente linea
#   Si no hay mas lineas devuelve espacios
print(">>>>   3.- Lectura de fichero con readline()  <<<<")
fichero1 = open("ejemplo.txt","r")
print(fichero1.readline())
print(fichero1.readline())
print(fichero1.readline())
fichero1.close()
#
#   Lectura con método readlines().
# 
#   El comando readlines devuelve una lista con todas
#   las lineas. Luego podemos recorrer la lista.
#   Si leemos una fila que no existe da error.
print(">>>>   4.- Lectura con readlines() y una lista  <<<<")
fichero1 = open("ejemplo.txt","r")
filas = fichero1.readlines()
print(filas[0])
print(filas[1])
print(filas[2])
fichero1.close()
#
#   Lectura y uso de la función list()
# 
#   Podemos usar list() para leer todas las filas en una lista
#
print(">>>>   5.- Lectura y uso de list()  <<<<")
fichero1 = open("ejemplo.txt","r")
filas = list(fichero1)
for i in filas:
    print(i)
fichero1.close()

    
    


