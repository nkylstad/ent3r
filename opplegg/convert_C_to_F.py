"""
Convert a data set of temperatures from 
degrees Celcius to degrees Fahrenheit.
"""

from numpy import *
from matplotlib import pyplot as plt

N = 395
filename = "temp_list.txt"
f = open(filename, 'r')
temperatures = zeros(N+1)
i = 0
for line in f:
	temperatures[i] = float(line)
	i += 1

size = len(temperatures)
x = linspace(0, size-1, size)

"""
Lager et plot av temperaturene i Celcius.
"""
plt.figure(1)
plt.plot(x, temperatures)
plt.xlabel("Dag nr."); plt.ylabel("Temperatur (C)")
plt.title("Temperaturvariasjon fra okt 2011 til okt 2012")

"""
Konverterer fra Celcius til Fahrenheit.
"""

temperatures_F = (9.0/5)*temperatures + 32
"""
Lager et plot av temperaturene i Fahrenheit.
"""
plt.figure(2)
plt.plot(x, temperatures_F)
plt.xlabel("Dag nr."); plt.ylabel("Temperatur (F)")
plt.title("Temperaturvariasjon fra okt 2011 til okt 2012")
plt.show()