import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./src/classificacao-imagens-dl/02-pandas/dataset/metrics.csv')

lista_epocas = range(1, len(df) + 1)

plt.figure(figsize=(10, 6))

plt.subplot(1,2,1)
plt.plot(lista_epocas, df['train_acc'], label='Train Acc', color='blue')

plt.plot(lista_epocas, df['val_acc'], label='Validation Acc', color='orange')
plt.title('Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.grid()

plt.subplot(1,2,2)
plt.plot(lista_epocas, df['train_loss'], label='Train Loss', color='blue')
plt.plot(lista_epocas, df['val_loss'], label='Validation Loss', color='orange')
plt.title('Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid()

plt.show()