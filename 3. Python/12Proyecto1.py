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
   *********************""")
while not fin:
    opc = int(input(" Opción:"))
    if opc == 1:
       num1 = int(input("Primer número  : "))
       num2 = int(input("Segundo número : "))
       print( "La suma es : ", num1 + num2)
    elif opc == 2:
       num1 = int(input("Primer número  : "))
       num2 = int(input("Segundo número : "))
       print( "La resta es : ", num1 - num2)
    elif opc == 3:
       num1 = int(input("Primer número  : "))
       num2 = int(input("Segundo número : "))
       print( "La multiplicación es : ", num1 * num2)     
    elif opc == 4:
       num1 = int(input("Primer número  : "))
       num2 = int(input("Segundo número : "))
       print( "La división es : ", num1 / num2)
    elif opc == 5:
        fin = True
    else:
       print( "Dame una opción válida. ")
    
