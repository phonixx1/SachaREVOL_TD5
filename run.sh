#!/bin/bash

# Check is venc package is install
if [ "$(pip3 freeze | grep virtualenv)" ]
then
	echo Package venv well installed
	echo
else
	echo First install virtualenv : "sudo pip3 install virtualenv "
	exit 1
fi

# Check if venv file is create : We consider we are on the TD5 file
fileEnv=.env
if [ -d "$fileEnv" ]
then
	echo Env already create
	echo
else
	virtualenv "$fileEnv"
fi

source "$fileEnv/bin/activate"

pip3 install -r requirements.txt # install the requirements

echo Dependencies well load
echo
echo Begining of .py script
echo
chmod +x mainFile.py           # give execution acces to the file main.py

./mainFile.py			# execute

echo End
