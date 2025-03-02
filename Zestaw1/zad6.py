from math import *

s = float( input('Podaj s: ') )
an = 1
a = 0
eps=1e-10

while True:
    a = an
    an = (s / a + a)/2
    if abs(a - an) < eps: break
print(an)
