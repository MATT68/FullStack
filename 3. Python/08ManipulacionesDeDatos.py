#
# Manipulaciones de cadenas de texto
# Eliminando espacios
#
texto1 = '  espacios a izquierda, y a derecha  ';
print(len(texto1));
print(texto1.lstrip());
print( len( texto1.lstrip() ) );
print(texto1.rstrip());
print( len( texto1.rstrip() ) );
print(texto1.strip());
print( len( texto1.strip() ) );
print('-----------------------');
#
# Seleccionando el menor y mayor caracter
#
texto1 = '  espacios a izquierda, y a derecha  ';
print(min(texto1));
print(max(texto1));
print('-----------------------');
texto2 = '12345abcdxyz';
print(min(texto2));
print(max(texto2));
print('-----------------------');
texto3 = '12345 ?%abcdxyz';
print(min(texto3));
print(max(texto3));
print('-----------------------');
#
# Sustitución de caracteres
#
texto1 = '  espacios a izquierda, y a derecha  ';
print(texto1.replace('e','X'));
#
# Inversión de mayúsculas y minúsculas
#
texto2 = 'NOMBRE matías APELLIDO andrés';
print(texto2);
print(texto2.swapcase());
#
# Trozeando una cadena en palabras
#
texto1 = '  espacios a izquierda, y a derecha  ';
print(texto1.split());
#
# Trozeando una cadena en palabras con separador
#
texto1 = '  espacios a izquierda, y a derecha  ';
print(texto1.split(','));
#


