#!/bin/bash
#  Primero preguntamos si el númeo de  parámetros ($#) es distinto (!) a 1 
if  ! [ $# -eq 1 ]
    then 
       echo "Dame un directorio como argumento"
else
#  Comprobamos si el parámetro recibido ($1) no es un directorio 
   if ! [ -d $1 ] 
      then 
           echo "El argumento debe ser un directorio "
   else
#  Si el parámetro es un directorio, entonces empezamos un bucle 
#  que recorre todos los archivos -en general- del directorio (ls $1)
      for  k  in  `ls $1`
      do
#  para cada archivo del directorio comprobamos si es un fichero ( -f $1/$k)
#  y si es así, contamos las líneas (wc -l < $1/$k)
        if [ -f $1/$k ]
           then 
#  Componemos una sola línea con varias informaciones           
            echo "Fichero : " $k  " Líneas : "  `wc -l < $1/$k`
        fi
      done
   fi
fi
