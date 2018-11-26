#print(vars())

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

#print(vars())

from numpy import cos, sin, linspace
#print(vars())

x = linspace (0, 4, 11)
y = sin(x)


print(vars())

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
plt.plot(x, y,)
plt.show()

