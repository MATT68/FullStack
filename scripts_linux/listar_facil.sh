for k in `ls $HOME/$1`
do
   wc -l  $HOME/$1/$k
done
