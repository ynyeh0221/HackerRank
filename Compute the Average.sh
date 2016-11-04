s=0
read N
for ((c=0; c<N; c++))
do
    read temp
    s=$((s+temp))
done
printf "%.3f" `echo $s/$N | bc -l`
