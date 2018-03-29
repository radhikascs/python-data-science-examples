from pylab import figure,polar,show
from numpy import arange,pi,cos

theta = arange(0,2,1./180)*pi
figure(1)

polar(3*theta,theta/5)
figure(2)

polar(theta,cos(4*theta))
# drawing the polar rose


show()