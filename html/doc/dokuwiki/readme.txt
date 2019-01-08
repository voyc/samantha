# The dokuwiki executable is installed in samwiki.
# The pages, media, and conf files are stored in samantha.
# Therefore, the wiki data is version-controlled by the github samantha project.
# And, the dokuwiki executable can be reinstalled, without risking loss of data. 

# In the webfaction control panel:
# samantha/ => samantha_aptr => webapps/samantha/samantha/html/
# samantha/wiki/ => samwiki_aptr => webapps/samwiki/docuwiki/

# Therefore, 
# samantha.voyc.com/ => webapps/samantha/samantha/html/index.html
# samantha.voyc.com/wiki => webapps/samwiki/dokuwiki/html/index.html

#The pages, media, and conf files are stored in 
#   webapps/samantha/samantha/html/doc/dokuwiki, 

# The following soft links redirect dokuwiki to samantha.
# start in dokuwiki folder
cd /home/jhagstrand/webapps/samwiki/dokuwiki

# add user css file, soft link to samantha github
ln -s /home/jhagstrand/webapps/samantha/samantha/html/doc/dokuwiki/conf/userall.css conf/userall.css

# add local entities file, soft link to samantha github
ln -s /home/jhagstrand/webapps/samantha/samantha/html/doc/dokuwiki/conf/entities.local.conf conf/entities.local.conf

# move pages, soft link to samantha github
ln -s /home/jhagstrand/webapps/samantha/samantha/html/doc/dokuwiki/data-pages data/pages

# move media, soft link to samantha github
ln -s /home/jhagstrand/webapps/samantha/samantha/html/doc/dokuwiki/data-media data/media
