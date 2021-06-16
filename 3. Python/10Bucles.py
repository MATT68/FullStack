#
#  Bucles
#
#   El bucle WHILE :
#
i = 0;
while i < 10:
    print(i,end=" ")
    i = i + 1
print(" \n Fin del bucle while !")
#
#   Otro bucle WHILE :
#
continuar = True
while continuar:
    Num = int(input("\nDame un número mayor de 50 :"))
    if Num > 50:
        continuar = False
print(" \n Fin del bucle while !")
#
#   Un bucle FOR :
#
lista1 = [1,2,3,4,5,6,7,8,9]
for i in lista1:
    print(i,sep = ' ',end = ' ')
print(" \n Fin del bucle FOR !")
#
#  Cuando finaliza el bucle WHILE -1-
#
i = 0;
j = 0;
while i < 10:
    print(i,end=" ")
    i = i + 1
j = j + 2
print(j,end=' ')
print(" \n Fin del bucle while -1- !")
#
#  Cuando finaliza el bucle WHILE -2-
#
i = 0;
j = 0;
while i < 10:
    print(i,end=" ")
    i = i + 1
    j = j + 2
    print(j,end=' ')
print(" \n Fin del bucle while -2- !")
