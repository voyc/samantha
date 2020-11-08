import mod1
print(mod1.x)

from mod1 import x
print(x)

from mod1 import x as y
print(y)

from mod1 import *
print(x)

import hello 
hello()
