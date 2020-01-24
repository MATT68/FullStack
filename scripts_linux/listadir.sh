if  test -d $1
then
	for file in `ls $1`
	do
	  echo 'Quieres borrar el fichero ? : '
	  ls -l  $1 $file
	  read borrar
	  if  test $borrar == 'S' -o $borrar == 's'
	      then rm -f $1/$file
	  else
	      echo 'Fichero no borrado'
	  fi
	done
fi
