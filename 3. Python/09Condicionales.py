#
# Las sentencias condicionales
#
# Simples :
Num = int(input(" Dame un número del 1 al 20 "));
if  Num > 20:
    print( "El número es mayor que 20");

print( "Has escrito el número :" + str(Num))
# -----------------
Frase = str(input("Escribe una frase :"));
if Frase.startswith('E'):
   print ("La frase empieza por 'E'");
#
# con else
#
if 'a' in Frase:
    print("Has escrito la letra 'a' ");
else:
     print("No contiene la letra 'a' ");
   
#
# con elif y else
#
PrimerNumero  = input("Dame un número : ");
SegundoNumero = input("Dame otro      : ");
if  PrimerNumero == SegundoNumero:
    print( " Son iguales !! ");
elif   PrimerNumero > SegundoNumero:
       print( str(PrimerNumero) + " es mayor que " + str(SegundoNumero) );
else:
       print( str(SegundoNumero) + " es mayor que " + str(PrimerNumero) );

              
