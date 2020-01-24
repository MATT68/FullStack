#!/bin/bash
# Este script pide un número y lo muestra si es mayor que 4
echo " Dame un número :" 
read a
if [ $a -gt 4 ]
   then 
       echo " El valor " $a "es mayor que 4!  " 
   else      
       echo " El valor " $a "no es mayor que 4!  " 
fi
