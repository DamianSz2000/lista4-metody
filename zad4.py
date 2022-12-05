import scipy as sp
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import optimize

np.seterr(all='ignore')

def f1(x, y):
    return x + math.e**(-x) + y**3

def f2(x, y):
    return x**2 + 2*x*y - y**2 + math.tan(x)

def derivf1x(x, y):
    return 1 - math.e**(-x)

def derivf2x(x, y):
    return 2*x + 2*y + 1/(math.cos(x)**2)

def derivf1y(x, y):
    return 3*y**2

def derivf2y(x, y):
    return 2*x - 2*y


def newton(x0):
    x1 = x0 - np.dot(np.linalg.inv(np.array([[derivf1x(x0[0][0], x0[1][0]), derivf1y(x0[0][0], x0[1][0])], [derivf2x(x0[0][0], x0[1][0]), derivf2y(x0[0][0], x0[1][0])]])), np.array([[f1(x0[0][0], x0[1][0])], [f2(x0[0][0], x0[1][0])]]))
    return x1

solutions = [[], []]
solutions = np.array(solutions)
eps = 0.000000001
for i in np.arange(-2, 2, 0.001):
    x0 = np.array([[i], [i]])
    while True:
        x1 = newton(x0)
        if (abs(f1(x1[0][0], x1[1][0])) <= eps and abs(f2(x1[0][0], x1[1][0])) <= eps) or (np.isnan(f1(x1[0][0], x1[1][0])) or np.isnan(f2(x1[0][0], x1[1][0]))):
            break
        x0 = x1
    if(x1[0][0] >= -2 and x1[0][0] <= 2 and x1[1][0] >= -2 and x1[1][0] <= 2):
        # append to solutions
        solutions = np.append(solutions, x1, axis=1)


#remove all duplicates
solutions = np.unique(solutions, axis=1)
#print pairs of solutions
for i in range(0, len(solutions[0])):
    print(f"x1: {solutions[0][i]} x2: {solutions[1][i]}")      





















# def jakobian(x,y):
#     J = [[1 - math.e**(-x), 3*y**2], [2*x+2*y+(math.cos(x)**(-2)), 2*x-2*y]]
#     return J


# x0 = np.array([[1], [1]])

# for i in range(40):
#     xn = x0 - (np.linalg.inv(jakobian(f1(x0[0][0], x0[1][0]), f2(x0[0][0], x0[1][0])))) * np.array([[f1(x0[0][0], x0[1][0])], [f2(x0[0][0], x0[1][0])]])
#     x0 = xn
#     print(x0)
