#
# Creación de una calculadora usando funciones
#
def Calculadora(opcion,Valor1,Valor2):
    if opcion == 1:
       Resultado = Suma(Valor1,Valor2)
    elif opc == 2:
       Resultado = Resta(Valor1,Valor2)
    elif opc == 3:
       Resultado = Multiplicacion(Valor1,Valor2)
    elif opc == 4:
       Resultado = Division(Valor1,Valor2)
    print( "El resultado es : ", Resultado)
    
def Suma(num1,num2):
    return num1 + num2

def Resta(num1,num2):
    return num1 - num2

def Multiplicacion(num1,num2):
    return num1 * num2

def Division(num1,num2):
    return num1 / num2


fin = False
print("""
   *********************
   C A L C U L A D O R A
   *********************

   Menú
   
   1) Suma
   2) Resta
   3) Multiplicación
   4) División
   5) Salir
   *********************
   """)
while not fin:
    opc = int(input("   Elige una opción : "))         
    if  opc in (1,2,3,4):
        Valor1 = int(input("Dame el primer número  : "))
        Valor2 = int(input("Dame el segundo número : "))
        Calculadora(opc,Valor1,Valor2)    
    elif  opc == 5:
        fin = True
    else:
       print( "Dame una opción válida. ")
    print( "\n")
    
