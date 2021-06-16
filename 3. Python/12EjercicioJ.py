nombreApellidos = 'Matías Andrés Pérez'
for i in 'áéíóú':
    if i == 'á':
        print(i)
        nombreApellidos = nombreApellidos.replace(i,'a')
    elif  i == 'é':
        print(i)
        nombreApellidos = nombreApellidos.replace(i,'e')   
    elif  i == 'í':
        print(i)
        nombreApellidos = nombreApellidos.replace(i,'i')   
    elif  i == 'ó':
        print(i)
        nombreApellidos = nombreApellidos.replace(i,'o')   
    else:
        print(i)
        nombreApellidos = nombreApellidos.replace(i,'u')
        
print(nombreApellidos)
    
