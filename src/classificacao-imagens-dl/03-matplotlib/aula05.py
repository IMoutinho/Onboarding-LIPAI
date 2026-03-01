import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y = x**5
y1 = x**2

# subplots
fig, ((ax1, ax2), (ax3, ax4 )) = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
plt.suptitle("Gráficos com Subplots")


ax1.plot(x, y)

ax2.plot(x, y1)

ax3.plot(x, y**3)

ax4.plot(x, y1**4)


plt.show()
