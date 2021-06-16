#
#   Más bucles ...........
#
#   Otro bucle FOR :
#
comidas = ["cocido","callos","huevos","patatas","pasta"]
for item in comidas:
    print(item.capitalize(),sep = ' ',end = '\n')
print(" \n Fin del bucle FOR !")
#
#   Uso de range para generar datos. Bucle FOR :
#
for item in range(14):
    print(item,sep = ' ',end = ' ')    
print(" \n Fin del bucle FOR con range !")
#
#   Anidamiento de bucles  FOR :
#
for i1 in range(5):
    for i2 in range(2,10,2):
        print(' i1 = ' + str(i1) +
              ' => i2 = ' + str(i2)) 
print(" \n Fin de los bucles FOR anidados !")
#
#   Anidamiento de bucles WHILE y FOR :
#
i1 = 0
while i1 < 5:
    for i2 in range(2,10,2):
        print(' i1 = ' + str(i1) +
              ' => i2 = ' + str(i2))
    i1 = i1 + 1    
print(" \n Fin de los bucles WHILE y FOR anidados !")
#
#   Anidamiento de bucles WHILE :
#
i1 = 0
while i1 < 5:
    i2 = 2
    while i2 < 10:
        print(' i1 = ' + str(i1) +
              ' => i2 = ' + str(i2))
        i2 = i2 + 2
    i1 = i1 + 1    
print(" \n Fin de los bucles WHILE anidados !")
