# Multiplos graficos em uma mesma figura com matplotlib


import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(-np.pi, np.pi, 100)
y = np.cos(t)
y1 = np.sin(t)

#Tudo que coloco entre plt.figure e plt.show, vai ser plotado na mesma figura, ou seja, no mesmo gráfico
plt.figure("Gráfico Cosseno - Seno", figsize=(6, 4))
plt.plot(t, y)
plt.plot(t, y1)
plt.title("Gráfico Cosseno - Seno")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.grid()

plt.show()

