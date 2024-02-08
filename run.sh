cd src
read debug
if [ "$debug" == "debug"] ;
then 
    python3 main.py -d
elif [ "$debug" == "custom" ]; 
then
    python3 main.py -c
else
    python3 main.py
    clear
fi