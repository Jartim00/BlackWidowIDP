#!/bin/bash
[[ $(whoami) != 'root' ]] && echo "run as sudo!" && exit 1
echo "The install will install packages with apt-get and pip. continue(y/n)"
read yn
[[ "$yn" == 'n' ]] && exit
apt-get install python-pygame
pip install flask
