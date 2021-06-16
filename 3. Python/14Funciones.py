#
#  Definición e invocación de una función
#  Sin parámetros de entrada ni salida
#
def Saludar():
    print(" Hola! cómo estamos?!\n")
Saludar()
#
#  Definición e invocación de una función
#  que no devuelve ningún valor
#
def EsUnaLetra(param):
    if  str(param).isalpha():
        print("Es una letra !")
    else:
            print("Ohhh, no es una letra !")
            
caracter = input("Teclea un caracter :")
EsUnaLetra(caracter)
#
#  Definición e invocación de una función
#  que admite parámetros y devuelve un valor
#
def Multiplicar(param1,param2):
    return param1 * param2
print(" Vamos a multiplicar : ")
num1 = int(input(" Dame un número entero   : "))
num2 = int(input(" Dame otro número entero : "))
resultado = Multiplicar(num1,num2)
print(" La multiplicación es : ",resultado)
#
#  Definición e invocación de una función
#  que admite parámetros y devuelve dos valores
#
def MultiplicarSumar(param1,param2):
    return param1 * param2, param1 + param2
print(" Vamos a multiplicar y sumar: ")
num1 = int(input(" Dame un número entero   : "))
num2 = int(input(" Dame otro número entero : "))
multiplicado,sumado = MultiplicarSumar(num1,num2)
print(" El resultado de la multiplicación es : ",
        multiplicado)
print(" El resultado de la suma es : ",sumado)
