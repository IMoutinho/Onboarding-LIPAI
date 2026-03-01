# customizando gráfico de linha
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 30)
y = np.cos(4*x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color="#E727F5", lw=0.5, marker="*", 
         ls = "dashdot")
plt.grid()
plt.title("Gráfico do Cosseno")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.show()
