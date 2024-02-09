cd src
read input
if [ "$input" == "d" ] ;
then 
    clear
    python3 main.py -d
elif [ "$input" == "c" ]; 
then
    clear
    python3 main.py -c
else
    clear
    python3 main.py
fi