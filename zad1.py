import scipy
import scipy.optimize
import numpy as np

def f(x):
    return 2*x**4+24*x**3+61*x**2-16*x+1


x = np.arange(-15, 15, 0.0001)

for i in x:
    if np.sign(f(i)) != np.sign(f(i+0.0001)):
        print(scipy.optimize.ridder(f, i, i+0.0001))

