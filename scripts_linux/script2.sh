# Este script pide un número y lo muestra si es mayor que 4
echo " Dame un número :" 
read a
if [ $a -gt 4 ]
   then 
       echo " El valor " $a "es mayor que 4!  " 
   elif [ $a -lt 4 ]
   then 
       echo " El valor " $a "es menor que 4!  " 
   else 
       echo " El valor " $a "es igual a   4!  " 
fi
