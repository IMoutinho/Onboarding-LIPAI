# identificando um ponto com linhas paralelas e marcador
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8-dark-palette")

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, lw=1.2, color="#E727F5")
axe.plot([0, 2.5], [0.4, 0.4], lw=1.2, color="gray", ls="--")
axe.plot([2.5, 2.5], [0, 0.4], lw=1.2, color="gray", ls="--")
axe.plot(2.5, 0.4, marker="*", color="#FF6347", markersize=8)
axe.set_xticks(np.arange(0, 5.5, 0.5))

plt.show()
