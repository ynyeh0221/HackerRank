read X
read Y
read Z

if [[ $X == $Y && $X == $Z ]]
then
    echo 'EQUILATERAL'
elif [[ $X == $Y || $Y == $Z || $X == $Z ]]
then
    echo 'ISOSCELES'
else
    echo 'SCALENE'
fi
