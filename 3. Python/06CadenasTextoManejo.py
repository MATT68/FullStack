# Manejo de cadenas de texto
#
Texto = 'no estoy seguro ni de qué día es hoy...'
print(Texto)
print(type(Texto))
#
# El método capitalize
print(Texto.capitalize())
#
# El método upper / lower
print(Texto.upper())
print(Texto.lower())
#
# Contando caracteres: len
# (primero vamos a provocar un error e interpretar la salida)
# print(Texto.len())
print(len(Texto))
##Vamos a investigar un momento la clase string y sus métodos:  
help(str)
##Y vamos a probar algunos : 
print(Texto.__len__())
Apendice = '...faltaba esto...'
print(Texto.__add__(Apendice))
print(Texto.endswith('.'))
print(Texto.count('o'))

