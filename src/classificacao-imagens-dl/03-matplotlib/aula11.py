# identificando um ponto com linhas paralelas e marcador
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8-dark-palette")

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, lw=1.2, color="#E727F5")

axe.text(2.6, 0.35, "P(2,5 ; 0,4)", fontsize=10, color="#FF6347")
axe.text(3, 0.42, "Logarítimo $y = log_{10}x$", fontsize=10, color="black",
         bbox=dict(facecolor="red", alpha=0.5))

axe.annotate("P(2,5 ; 0,4)", xy=(2.5, 0.4), fontsize=16, xytext=(
    0.5, 0.5), arrowprops=dict(facecolor="#2EB821D3"), color="#214EB8")

axe.plot([0, 2.5], [0.4, 0.4], lw=1.2, color="gray", ls="--")
axe.plot([2.5, 2.5], [0, 0.4], lw=1.2, color="gray", ls="--")
axe.plot(2.5, 0.4, marker="*", color="#FF6347", markersize=8)
axe.set_xticks(np.arange(0, 5.5, 0.5))
axe.set_title("Gráfico do Logaritmo", fontsize=15, color="#E727F8")
axe.set_xlabel("Valor de x", fontsize=12, color="#20B2AA")
axe.set_ylabel("Valor de log10(x)", fontsize=12, color="#20B2AA")

plt.grid()
plt.show()
