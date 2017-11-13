# local modifications to dokuwiki for samantha

# start in dokuwiki folder
cd /home/jhagstrand/webapps/samwiki/dokuwiki

# add user css file, soft link to samantha github
ln -s /home/jhagstrand/webapps/samantha/html/doc/dokuwiki/conf/userall.css conf/userall.css

# add local entities file, soft link to samantha github
ln -s /home/jhagstrand/webapps/samantha/html/doc/dokuwiki/conf/entities.local.conf conf/entities.local.conf

# move pages, soft link to samantha github
mv data/pages data/pages-org
ln -s /home/jhagstrand/webapps/samantha/html/doc/dokuwiki/data-pages data/pages

# move media, soft link to samantha github
mv data/media data/media-org
ln -s /home/jhagstrand/webapps/samantha/html/doc/dokuwiki/data-media data/media
