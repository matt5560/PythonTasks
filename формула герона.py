import math

def formula_gerona(a,b,c):
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S

print(formula_gerona(3,4,5))
