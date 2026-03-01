# customizando as escalas do eixo do grafico

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 300)
y = np.cos(3*x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y)

axe.set_title("Gráfico do Cosseno", fontsize=15, color="#E727F8")
axe.set_xlabel("Tempo", fontsize=12, color="#20B2AA")
axe.set_ylabel("Amplitude", fontsize=12, color="#20B2AA")

plt.xticks(np.arange(0, 2*np.pi+0.5, 0.5), fontsize=8, color="#FF6347")
plt.yticks(np.arange(-1, 1.2, 0.2), fontsize=8, color="#FF6347")

plt.grid()
plt.show()
