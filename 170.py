from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)

k = 0
a = 1.1
b = 3.2

funa = f(a)
funb = f(b)

if ( funa * funb > 0.0) :
    print "dotajDotajaa intervaalaa [%s, %s] saknju nav"%(a,b)
    sleep(1); exit()
else:
    print "Dotaja intervala sakne(s) ir"

deltax = 0.01

while ( fabs(b-a) > deltax ):
    k = k+1
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x
print "sakne ir :", x
print "Y koordinates vertiba ir: ", sin(x)
print("Iteraciju skaits: ", k)
