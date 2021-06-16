#
#  Funciones que reciben una lista como parámetros
#
def Sumar(*Valores):
    resultado = 0
    for item in Valores:
        resultado = resultado + item
    return resultado
Total = Sumar(5,7,8)
print("La suma de todo es : ", Total)
#
#  Funciones anidadas
#
def SumarRestar(param1, param2):
    return Sumar(param1,param2), Restar(param1,param2)

def Sumar(sumando1, sumando2):
    return sumando1 + sumando2

def Restar(minuendo, sustraendo):
    return minuendo - sustraendo
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
resultadosuma, resultadoresta = SumarRestar(numero1,numero2)

print("El resultado de la suma es: ", resultadosuma)
print("El resultado de la resta es: ", resultadoresta)
