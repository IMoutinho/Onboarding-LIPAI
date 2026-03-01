import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y = x**5
y1 = x**2

# subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
plt.suptitle("Gráficos com Subplots")

plt.subplots_adjust(
    left=0.152,
    right=0.943,
    top=0.9,
    bottom=0.14,
    wspace=0.438,
    hspace=0.4
)

axes[0, 0].plot(x, y)
axes[0, 0].set_title("Gráfico x^5")
axes[0, 0].set_xlabel("Tempo")
axes[0, 0].set_ylabel("Amplitude")
axes[0, 0].grid(True)

axes[0, 1].plot(x, y1)
axes[0, 1].set_title("Gráfico x^2")
axes[0, 1].set_xlabel("Tempo")
axes[0, 1].set_ylabel("Amplitude")
axes[0, 1].grid(True)

axes[1, 0].plot(x, y**3)
axes[1, 0].set_title("Gráfico x^15")
axes[1, 0].set_xlabel("Tempo")
axes[1, 0].set_ylabel("Amplitude")
axes[1, 0].grid(True)

axes[1, 1].plot(x, y1**4)
axes[1, 1].set_title("Gráfico x^8")
axes[1, 1].set_xlabel("Tempo")
axes[1, 1].set_ylabel("Amplitude")
axes[1, 1].grid(True)

plt.show()
