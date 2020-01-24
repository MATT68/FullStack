if  ! [ $# -eq 1 ]
    then 
       echo "Dame un directorio como argumento"
else
   if ! [ -d $1 ] 
      then 
           echo "El argumento debe ser un directorio "
   else
      for  k  in  `ls $1`
      do
        if [ -f $1/$k ]
           then 
            echo "Fichero : " $k  " Líneas : "  `wc -l < $1/$k`
        fi
      done
   fi
fi
    
