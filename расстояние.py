import math
from math import sqrt
def distance(x1,y1,x2,y2):
    c = (x1-x2)**2 + (y1-y2)**2
    
    return sqrt(c)
    
x1 = int(input("x1 "))
y1 = int(input("y1 "))
x2 = int(input("x2 "))
y2 = int(input("y2 "))
    
distance(x1,y1,x2,y2)
print(distance(x1,y1,x2,y2))
