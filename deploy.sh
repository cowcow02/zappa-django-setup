#!/bin/bash

export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
echo 'region = us-east-1' >> ~/.aws/config

pip install -q virtualenv
sudo add-apt-repository ppa:jonathonf/python-3.6 -y
sudo apt-get -qq update
sudo apt-get -qq install python-dev
sudo apt-get -qq install python3.6-dev

virtualenv -p /usr/bin/python3.6 ve;
. ve/bin/activate;
pip install -q zappa;
pip install -q -r requirements.txt;
zappa deploy $1;
zappa update $1;

zappa manage $1 "migrate --noinput"
python manage.py collectstatic --noinput
deactivate;