import scipy as sp
import numpy as np
import math
import matplotlib.pyplot as plt

#f(t) = V(t) - Vs
#f'(t) = (u*m)/(M0-m*t) -g
#t(k+1) = tk - f(t)/f'(t)

def tk(u, M0, m, g, t):
    return (u*math.log((M0)/(M0-m*t), math.e)-g*t)-335

def tkprim(u, M0, m, g, t):
    return (u*m)/(M0-m*t) - g


u = 2510
M0 = 2.8e6
m = 13.3e3
g = 9.81

x = []
y = []
x = np.array(x)
y = np.array(y)

v = 1
t = 1
while v != 0:
    tk1 = t - (tk(u, M0, m, g, t))/(tkprim(u, M0, m, g, t))
    t = tk1
    v = tk(u, M0, m, g, tk1)

print(f"Czas po ktorym rakietka osiagnie predkosc 335m/s to {t} sekund")


