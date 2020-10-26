# build icon

# compile the js files with google closure compiler
python compilejs.py $1 >min.js

# compress css file with yui
cat normaleyes.css icon/icon.css minimal.css |
  sed 's/+/%2b/g'  >min.css
wget --post-data="input=`cat min.css`" --output-document=min.css https://cssminifier.com/raw

# prepare index.php for production use
cp index.html index.php
sed -i -e 's/<!--<remove>//g' index.php
sed -i -e 's/<remove>-->//g' index.php
