#!/bin/sh
# launcher1.sh
# navigeert naar home map, dan naar deze map, daarna voert hij de script uit 
# en gaat vervolgens weer naar de home map

cd /home/pi/Documents/Controller
sudo python Screen.py
echo 'succesful'  > /home/pi/Documents/succesful.txt
