#!/bin/bash
# Este script crea un directorio y dentro de él, un fichero.
# Debe recibir como parámetros el directorio y el fichero
if  test $# -eq 2
    then
	if test ! -d $HOME/$1
           then 
                mkdir $HOME/$1
        else
           echo "El directorio " $HOME/$1 " ya existe! "
        fi

       touch $HOME/$1/$2
   else 
       echo " Este script crea un directorio y un fichero " 
       echo " Debe recibir como primer parametro el directorio " 
       echo " y como segundo parametro el fichero con extension " 
       echo " --------------------------------------------- " 
fi
