#!/usr/bin/bash

SRCDIR=/home/john/webapps/samantha/samantha/python
CHATSERVER=samchat.py
HTTPSERVER=samhttp.py
LOG=/var/log/user/sam/sam.log
DOCROOT=/home/john/webapps/samantha/samantha/html

if [ $1 == 'http' ]; then
	cd $DOCROOT
	python3 $SRCDIR/$HTTPSERVER &>>$LOG
elif [ $1 == 'chat' ]; then
	python3 $SRCDIR/$CHATSERVER &>>$LOG
else
	echo 'usage:  samweb.sh [http | chat]'
fi
