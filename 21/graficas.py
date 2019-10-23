from numpy import *
from matplotlib.pylab import *

t=linspace(0,2*pi,100)
cosi = lambda t: cos(t)

plot(cosi(t))
savefig('cos.png')