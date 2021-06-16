#
# Validaciones sobre cadenas de texto
#
cadena1 = 'hola12345'
cadena2 = 'hola 12345'
cadena3 = 'hola?12345'
cadena4 = 'hola'
cadena5 = '12345'
#
# Validamos si contienen sólo caracteres alfanuméricos
print(cadena1.isalnum());
print(cadena2.isalnum());
print(cadena3.isalnum());
print(cadena4.isalnum());
print(cadena5.isalnum());
print('----------------------')
#
# Validamos si contienen sólo caracteres alfabéticos
print(cadena1.isalpha());
print(cadena2.isalpha());
print(cadena3.isalpha());
print(cadena4.isalpha());
print(cadena5.isalpha());
print('----------------------')
#
# Validamos si contienen sólo caracteres numéricos
print(cadena1.isdigit());
print(cadena2.isdigit());
print(cadena3.isdigit());
print(cadena4.isdigit());
print(cadena5.isdigit());
print('----------------------')
#
# Validamos si contienen sólo minúsculas
print(cadena1.islower());
print(cadena2.islower());
print(cadena3.islower());
print(cadena4.islower());
print(cadena5.islower());
print('----------------------')
