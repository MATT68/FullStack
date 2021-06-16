import random
a = int(input('Dame un número del 1 al 100 : '))
b =  random.randint(1,100)
continuar = True
while continuar:
    if  a > b :
        print('Te has pasado ...')
        a = int(input('Vuelve a intentarlo : '))
    elif a < b :
        print('... te has quedado corto ...')
        a = int(input('Vuelve a intentarlo : '))
    else:
        print('Efectivamente, el número era : ' , b)
        continuar = False
        

    
