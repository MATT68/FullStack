# Vamos a jugar a multiplicar (con enteros).
# Para ello definimos algunas funciones : 
def multiplicar(n,m):
    producto = n * m 
    print('\t > > > > > > > > > > > > > > > > > > > > > >  ')
    print(' \t El resultado es : ') 
    print(' \t\t    ',n) 
    print(' \t\t  X ',m) 
    print(' \t\t -------') 
    print(' \t\t    ',producto)

def dividir(n,m):
    cociente = n // m
    resto    = n %  m 
    print('\t > > > > > > > > > > > > > > > > > > > > > >  ')
    print(' \t El resultado es : ') 
    print(' \t\t    ',n, ' |_',m,'_______') 
    print(' \t\t           ',cociente) 
    print(' \t\t      ',resto)

def sumar(n,m):
    sumatorio = n + m 
    print('\t > > > > > > > > > > > > > > > > > > > > > >  ')
    print(' \t El resultado es : ') 
    print(' \t\t    ',n) 
    print(' \t\t  + ',m) 
    print(' \t\t -------') 
    print(' \t\t    ',sumatorio)

def restar(n,m):
    resta = n - m 
    print('\t > > > > > > > > > > > > > > > > > > > > > >  ')
    print(' \t El resultado es : ') 
    print(' \t\t    ',n) 
    print(' \t\t  - ',m) 
    print(' \t\t -------') 
    print(' \t\t    ',resta)

def elegirOpcion():
    continuar = True
    while continuar:
        try:
            opcion = int(input('¿Qué quieres hacer ? : '))
            if  opcion >= 0 and opcion <= 5 :
                continuar = False
            else:  
                print('Esa no es una opción válida')    
        except:        
            print('Esa no es una opción válida')    
    return(opcion)

def pedirNumeros():
    continuar = True
    while continuar:
        try: 
            a = int(input('Dame el primer número : '))
            b = int(input('Dame el segundo  número : '))
            continuar = False
        except: 
            print(' Eso no es un número entero!') 
    return(a,b)        

def opcionEnConstruccion():
    print(" Esa opción aún no está lista, puedes probar otra ... ")

# Comienzo del programa:
nombre = input('¿Cómo te llamas? : ')
print('Hola ', nombre, ' soy tu calculadora personal!!. ')
Calcular = True
while Calcular:
    print('\t > > > > > > > > > > > > > > > > > > > > > >  ')
    print('\t Elige la opción que deseas : ')
    print('\t\t 1.- Multiplicar. ')
    print('\t\t 2.- Dividir. ')
    print('\t\t 3.- Restar. ')
    print('\t\t 4.- Sumar. ')
    print('\t\t 5.- Salir. ')
    print('\t > > > > > > > > > > > > > > > > > > > > > >  ')

    opcion = elegirOpcion()
    Operacion = {1:"Multiplicar",
                2:"Dividir",
                3:"Restar",
                4:"Sumar",
                5:"Terminar"}

    print(' Vale, vamos a  ',  Operacion[opcion],' !! ') 

    if  opcion != 5:
        (a,b) = pedirNumeros()

    if  opcion == 1:
        multiplicar(a,b)    
    elif opcion == 2:
        dividir(a,b)    
    elif opcion == 3:
        restar(a,b)    
    elif opcion == 4:
        sumar(a,b)    
    elif opcion == 5:
        Calcular = False




