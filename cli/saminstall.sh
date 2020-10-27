#!/usr/bin/bash

# install to systemd
sudo cp /home/john/webapps/samantha/samantha/cli/samweb.sh /usr/local/bin/
sudo cp /home/john/webapps/samantha/samantha/cli/samchat.service /lib/systemd/system/
sudo cp /home/john/webapps/samantha/samantha/cli/samhttp.service /lib/systemd/system/
sudo cp /home/john/webapps/samantha/samantha/cli/samweb.target /lib/systemd/system/

# sudo systemctl start samweb
# sudo systemctl stop samweb
# sudo systemctl status samweb
# sudo systemctl enable samweb
