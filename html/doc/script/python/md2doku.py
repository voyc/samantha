# markdown to dokuwiki conversion
# usage:
#    python md2doku.py <Conceptual-Design.md   >conceptual_design.txt

import fileinput
import regex as re
 
for line in fileinput.input():
    # headings
    line = re.sub(r'^#### (.*)$', r'== \1 ==', line)
    line = re.sub(r'^### (.*)$',  r'== \1 ==', line)
    line = re.sub(r'^## (.*)$', r'==== \1 ====', line)
    line = re.sub(r'^# (.*)$',  r'==== \1 ====', line)

    # images
    line = re.sub(r'\!\[(.*)\]\(http\:\/\/samantha\.voyc\.com\/doc\/image\/plot\/(.*)\)', r'{{\2|\1}}', line)
    line = re.sub(r'\!\[(.*)\]\(http\:\/\/samantha\.voyc\.com\/doc\/image\/equation\/(.*)\)', r'$$\1$$', line)
    line = re.sub(r'\.png\#[123]', r'.png', line)

    # lists
    line = re.sub(r'^\* ',  r'  * ', line)
    line = re.sub(r'^1\. ', r'  - ', line)

    # italics
    line = re.sub(r'_(.*?)_', r'//\1//', line)

    # line endings
    line = re.sub(r'  $', r'\\\\', line)
    line = line.rstrip()
    print(line)
