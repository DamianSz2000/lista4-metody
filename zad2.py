import scipy
import numpy


a = float(input("Podaj liczbe dodatnia: "))
x0 = 1

for i in range(5):
    x0 = x0 - ((x0**5 - a)/(5*x0**4))

print(f"Pierwiastek piatego stopnia z {a} to {x0}") #ja petle powtorzylem 5 razy i otrzymalem dosc dokladny wynik, im więcej iteracji tym dokładniejszy wynik

