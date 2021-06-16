# Tipos de datos: Cadenas (de texto)
#
# Manejando cadenas
cadena1 = "Comienza el ejercicio";
print(cadena1);
# Caracteres de escape
cadena2 = "Continua el ejercicio \n Y ahora en líneas \n diferentes";
print(cadena2);
#
# Tipos de datos:
#  Colecciones: Listas 
#
lista1=["árbol","bola","muñeco"]
print(lista1);
print(len(lista1));
print(lista1[0]);
print(lista1[1]);
print(lista1[2]);
#
# Uniones -suma- de listas
#
lista2=["estrella","cinta","reno"]
ListaTotal = lista1 + lista2;
print(ListaTotal)
#
# Agregar elementos a una lista
#
lista2 = lista2 + ["oveja"]
print(lista2)
#
# Eliminar un elemento de una lista
#
print(lista2)
del lista2[2]
print(lista2)
#
# Modificar elementos de una lista
#
lista2[0]="corcho"
lista2[1]="madera"
lista2[2]="metal"
print(lista2)
#
# Las listas contienen todo tipo de datos.
# Hasta otras listas:
#
lista = ["avenida","calle","plaza",["fuente","banco","paloma"]]
print(lista);
print(lista[0]);
print(lista[1]);
print(lista[2]);
print(lista[3]);
print(lista[3][0]);
print(lista[3][1]);
print(lista[3][2]);
#
# Tuplas : conjunto de elementos ordenados e inmutables
#
tupla = ("recta","circulo","cuadrado");
print(tupla);
print(len(tupla));
print(tupla[0]);
print(tupla[1]);
print(tupla[2]);
# un error común ....
# del tupla[1];
print(tupla);
#
# Diccionarios : listas de clave valor
#
LeeNumeros = {"1":"uno",
              "2":"dos",
              "3":"tres",
              "4":"cuatro",
              "5":"cinco",
              "6":"seis",
              "7":"siete",
              "8":"ocho",
              "9":"nueve",
              "0":"cero"};
print(LeeNumeros["2"])              
print(LeeNumeros["9"])              

