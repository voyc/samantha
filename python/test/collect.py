
list = [1,2,3,4]
tuple = (1,2,3,4)
set = {1,2,3,4,1,2}

print (list)
print (tuple)
print (set)

from collections import namedtuple

color = namedtuple('color', ['r', 'g', 'b']) 
white = color(255,255,255)
print(white.r)

