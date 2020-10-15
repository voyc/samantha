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

# install to systemd
# sudo ln -s /home/john/webapps/samantha/samantha/cli/samweb.sh /usr/local/bin/samweb.sh
# sudo ln -s /home/john/webapps/samantha/samantha/cli/samchat.service /lib/systemd/system/samchat.service
# sudo ln -s /home/john/webapps/samantha/samantha/cli/samhttp.service /lib/systemd/system/samhttp.service
# sudo ln -s /home/john/webapps/samantha/samantha/cli/samweb.target /lib/systemd/system/samweb.target

# sudo systemctl start samweb
# sudo systemctl stop samweb
# sudo systemctl status samweb
# sudo systemctl enable samweb
