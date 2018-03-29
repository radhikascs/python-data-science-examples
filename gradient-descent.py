from sympy import *
import numpy as np
from matplotlib import pyplot as plt

x = Symbol('x')
y = x**2
yprime = y.diff(x)
ypp = yprime.diff(x)

def plotFun():
    space = np.linspace(-5,5,100)
    data = np.array([N(y.subs(x,value)) for value in space])
    plt.plot(space, data)
    plt.show()

theta = 84
theta2 = 0
alpha = .01
iterations = 0
check = 0
precision = 1/1000000
plot = True
iterationsMax = 10000
maxDivergence = 50

while True:
    theta2 = theta - alpha*N(yprime.subs(x,theta)).evalf()
    iterations += 1
    if iterations > iterationsMax:
        print("Too much iterations")
        break
    if theta < theta2:
        print("The value of theta is diverging")
        check += 1
        if check > maxDivergence:
            print("Too much iterations (%s), the value of theta is diverging"%maxDivergence)
            print("Please choose a smaller alpha and, or check that the function is indeed convex")
            plot = False
            break
    if abs(theta - theta2) < precision:
        break
    
    theta = theta2


if plot:
    print("Number of iterations:",iterations,"value of theta:",theta2,sep=" ")
    plt.title("Gradient Descent Illustration")
    plt.plot(theta,N(y.subs(x,theta)).evalf(),marker='o',color='r')
    plotFun()